# -*- coding: utf-8 -*-
from ultralytics import YOLO
import numpy as np
import cv2
import torch
# 导入已经训练好的模型
model = YOLO('./runs/detect/train7/weights/best.pt')

# 执行预测
results = model.predict('./test1.jpg', conf=0.1, imgsz=1280, save=True)

# 获取图片的宽度和高度
image_path = './test1.jpg'
image = cv2.imread(image_path)
height, width, _ = image.shape

# 获取图片名称（不带路径和后缀）
image_name = 'test1'


# 保存推理结果为 YOLOv8 格式的 TXT 文件
def save_results_to_txt(results, image_name, img_width, img_height):
    txt_path = f'./runs/detect/{image_name}.txt'
    with open(txt_path, 'w') as f:
        for result in results:
            for box in result.boxes:
                # 获取预测类别和坐标
                cls = int(box.cls.cpu().numpy())
                xywh = box.xywh.cpu().numpy()

                x_center, y_center, box_width, box_height = xywh[0]

                # 归一化坐标
                x_center /= img_width
                y_center /= img_height
                box_width /= img_width
                box_height /= img_height

                # 将结果按 YOLOv8 格式保存
                f.write(f'{cls} {x_center} {y_center} {box_width} {box_height}\n')


# 调用保存结果函数
save_results_to_txt(results, image_name, width, height)