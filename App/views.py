import os

import cv2 as cv
import numpy as np
from django.http import HttpResponse
from django.shortcuts import render

from App.FaceRecognition.FaceRecognition import FaceRecognition
from App.FaceRecognition.FaceTrainer import FaceTrainer
from App.MysqlHelper import MysqlHelper


# Create your views here.
def home(request):
    # return HttpResponse("欢迎使用")
    name = "胡歌"
    return render(request, 'Home.html', {'n1': name})


def faceEntering(request):
    if request.method == 'GET':
        return render(request, 'faceEntering.html')
    if request.method == 'POST':
        if request.POST.get('train') == '1':
            faceTrainer = FaceTrainer()
            faceTrainer.train()
            return render(request, 'faceEntering.html', {'train': '训练完成'})
        else:
            # 由前端指定的name获取到图片数据
            imgs = request.FILES.getlist('img')
            name = request.POST.get('name')
            for img in imgs:
                sql = MysqlHelper()
                id = np.random.randint(1e0, 1e8)
                label = sql.FindLabel(id)
                while not label.empty:
                    id = np.random.randint(1e0, 1e8)
                    label = sql.FindLabel(id)
                sql.InsertLabel(id, name)
                # 重定义文件名
                img_name = f'{str(id)}{".png"}'
                # 从配置文件中载入图片保存路径
                img_path = os.path.join('ImageData/train/', img_name)
                # 写入文件
                with open(img_path, 'ab') as fp:
                    # 如果上传的图片非常大，就通过chunks()方法分割成多个片段来上传
                    for chunk in img.chunks():
                        fp.write(chunk)
            return render(request, 'faceEntering.html', {'submit': '录入完成'})


def faceRecognition(request):
    if request.method == 'GET':
        # file_one=open()
        return render(request, 'faceRecognition.html')
    if request.method == 'POST':
        img = request.FILES.get('img')
        img_name = f'{"test"}{".png"}'
        # 从配置文件中载入图片保存路径
        img_path = os.path.join('ImageData/test/', img_name)
        with open(img_path, 'wb') as fp:
            # 如果上传的图片非常大，就通过chunks()方法分割成多个片段来上传
            for chunk in img.chunks():
                fp.write(chunk)
        img_re = cv.imread(img_path)
        re = FaceRecognition()

        img_result, name = re.Recongnition(img_re)
        return render(request, 'faceRecognition.html', {'result': name})
