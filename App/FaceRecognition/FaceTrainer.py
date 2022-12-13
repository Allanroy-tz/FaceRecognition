import os
import numpy as np
import cv2 as cv
from PIL import Image

from App.FaceRecognition.FaceDetector import FaceDetector


class FaceTrainer:
    trainer_path = '../../trainer/trainer.yml'

    img_path = '../../ImageData/train'

    def GetImageAndLabels(self, path):
        # 存储人脸信息
        face_samples = []
        # 存储姓名数据
        ids = []
        # 存储图片信息
        image_paths = [os.path.join(path, r) for r in os.listdir(path)]
        # 加载分类器
        face_detector = FaceDetector()
        # 遍历列表中的图片
        for imagePath in image_paths:
            # 打开图片,灰度化 PIL:1,L,P,RGB,RGBA,CMYK,YCbCr,I,F
            pil_img = Image.open(imagePath).convert('L')
            # 将图片转换为数组,以黑白深浅
            img_numpy = np.array(pil_img, 'uint8')
            # 获取图片人脸特征
            faces = face_detector.ImgFaceDetect(img_numpy)
            # 获取每张图片的id和姓名
            id = int(os.path.split(imagePath)[1].split('.')[0])
            # 预防无面容照片
            for x, y, w, h in faces:
                ids.append(id)
                face_samples.append(img_numpy[y:y + h, x:x + w])
        print('id', id)
        print('fs', face_samples)
        return face_samples, ids

    def train(self):
        faces, ids = self.GetImageAndLabels(self.img_path)
        # 加载识别器
        recognizer = cv.face.LBPHFaceRecognizer_create()
        # 训练
        recognizer.train(faces, np.array(ids))
        # 保存文件
        recognizer.write(self.trainer_path)

trainer=FaceTrainer()
trainer.train()