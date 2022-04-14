#yolo v5 학습을 위한 train / valid 나누기!

import cv2.cv2
import tensorflow as tf
from glob import glob

img_list = glob("/factory/dataset/images/*.jpg")

from sklearn.model_selection import train_test_split

train_img_list, val_img_list = train_test_split(img_list, test_size=0.2, random_state=2000)

with open('/factory/dataset/train.txt','w') as f:
    f.write('\n'.join(train_img_list)+'\n')

with open('/factory/dataset/val.txt','w') as f:
    f.write('\n'.join(val_img_list)+'\n')


import yaml

with open("/factory/dataset/factory_dataset.yaml", 'r') as f:
    data = yaml.load(f)

data['train'] = '/factory/dataset/train.txt'
data['val'] = '/factory/dataset/val.txt'

with open('/factory/dataset/factory_dataset.yaml', 'w') as f:
    yaml.dump(data, f)

# Train YOLOv5s on COCO128 for 3 epochs
#python train.py --img 640 --batch 16 --epochs 50 --data /factory/dataset/factory_dataset.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --name obj_results




