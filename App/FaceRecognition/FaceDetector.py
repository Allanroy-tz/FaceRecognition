import cv2 as cv


class FaceDetector:
    face_detect = cv.CascadeClassifier('D:/OpenCV/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')

    def ImgFaceDetect(self, img):
        face = self.face_detect.detectMultiScale(img)
        return face

    def DrawFace(self, img):
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face = self.ImgFaceDetect(img_gray)
        print(face)
        for x, y, w, h in face:
            cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        return img


# img = cv.imread('../../ImageData/mcs.jpg')
# detector = FaceDetector()
# img = detector.DrawFace(img)
# cv.imshow("test", img)
# cv.waitKey(0)
# cv.destroyAllWindows()