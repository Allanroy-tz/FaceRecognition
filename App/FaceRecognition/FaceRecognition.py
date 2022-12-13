import cv2 as cv
import numpy as np

from PIL import ImageFont, ImageDraw, Image

from App.FaceRecognition.FaceDetector import FaceDetector


class FaceRecognition:
    recogizer = cv.face.LBPHFaceRecognizer_create()
    recogizer.read('../../trainer/trainer.yml')

    def Recongnition(self, img):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face_detector = FaceDetector()
        # face=face_detector.detectMultiScale(gray,1.1,5,cv.CASCADE_SCALE_IMAGE,(100,100),(300,300))
        face = face_detector.ImgFaceDetect(gray)
        img_cv = Image.fromarray(img)
        font1 = ImageFont.truetype("C:/Windows/Fonts/simsun.ttc", 100)
        draw = ImageDraw.Draw(img_cv)
        for x, y, w, h in face:
            cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
            cv.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 0), thickness=1)
            # 人脸识别
            ids, confidence = self.recogizer.predict(gray[y:y + h, x:x + w])
            print("标签id:", ids, "置信评分:", confidence)
            if confidence > 80:
                draw.text((10, 10), "未知人脸", font=font1, fill=(0, 0, 255))
            else:
                draw.text((10, 10), '2', font=font1, fill=(0, 0, 255))
        img = np.array(img_cv)
        cv.imshow("result", img)
        return img

img=cv.imread('../../ImageData/mcs.jpg')
recogizer=FaceRecognition()
recogizer.Recongnition(img)
cv.waitKey(0)
cv.destroyAllWindows()
