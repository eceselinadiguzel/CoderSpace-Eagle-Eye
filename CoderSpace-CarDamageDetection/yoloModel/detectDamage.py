########################################################################
# IMPORT LIBS
import argparse
import time
from pathlib import Path
import cv2
import numpy as np
import torch
import torch.backends.cudnn as cudnn
from PyQt5.QtGui import QImage, QPixmap
from numpy import random

from models.experimental import attempt_load
from utils2.datasets import LoadStreams, LoadImages
from utils2.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils2.plots import plot_one_box
from utils2.torch_utils import select_device, load_classifier, time_synchronized
import numpy
import torch
import os
from ultralytics import YOLO
########################################################################
# IMPORT YOLO MODEL
current_directory = os.getcwd()
model_path = os.path.join(current_directory, r'yoloModel\bestCarDamageClass.pt')
model = YOLO(model_path)
########################################################################
# GLOBAL DECLARATION
txt = ""
########################################################################

def detect(imgnew, save_img=False):
    global txt
    imgnew2 = imgnew
    view_img = True
    results = model(imgnew2)


    for i, det in enumerate(results[0].boxes.data):
        detlist = []
        if(numpy.array(det[4])>=0 and int(numpy.array(det[5]))==0): # agir
            txt = "Agir Hasarli"
            for k in range(0, 4):
                detlist.append(det[k])
                print("")
        elif (numpy.array(det[4]) >= 0 and int(numpy.array(det[5])) == 1):  # az
            txt = "Az Hasarli"
            for k in range(0, 4):
                detlist.append(det[k])
                print("")
        elif (numpy.array(det[4]) >= 0 and int(numpy.array(det[5])) == 2):  # saglam
            txt = "Hasarsiz"
            for k in range(0, 4):
                detlist.append(det[k])
                print("")
        elif (numpy.array(det[4]) >= 0 and int(numpy.array(det[5])) == 3):  # orta
            txt = "Orta Hasarli"
            for k in range(0, 4):
                detlist.append(det[k])
                print("")
        else:
            continue
        plot_one_box(detlist, imgnew, color = (0,0,255), line_thickness=500000)


    if view_img:
        # font
        font = cv2.FONT_HERSHEY_DUPLEX
        # org
        org = (35, 40)
        # fontScale
        fontScale = 2
        # Blue color in BGR
        color = (255, 0, 0)
        # Line thickness of 2 px
        thickness = 4
        imgnew = cv2.putText(imgnew, txt,org, font,fontScale, color, thickness, cv2.LINE_AA)

    return imgnew


def main(img2):
    im0 = detect(img2)
    return im0


