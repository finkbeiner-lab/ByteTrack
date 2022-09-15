import os
import pdb
import glob
import cv2
import pandas as pd
from skimage import io
import numpy as np
from skimage.draw import rectangle


DATA_PATH = "/home/vivek/Projects/ByteTrack/datasets/FinkbeinerTrack/AB7-SOD1-KW4-WTC11-Survival-exp3"
SAVE_DIR = "/home/vivek/Projects/ByteTrack/results"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

wells = glob.glob(os.path.join(DATA_PATH, "*"))
for well in wells:

    print(os.path.basename(well))
    RESULT_SAVE_PATH = os.path.join(SAVE_DIR, os.path.basename(well))

    if not os.path.exists(RESULT_SAVE_PATH):
        os.makedirs(RESULT_SAVE_PATH)

    well_images = glob.glob(os.path.join(well, "*.tif"))
    gt = pd.read_csv(os.path.join(well, "groundtruth.csv"))

    well_images = sorted(well_images)

    for well_image in well_images:
        
        # read image as it is ( 16bit format)
        img = cv2.imread(well_image, -1)
        img_name = os.path.basename(well_image)
        y = img_name.split("_")
        timepoint = int(y[2][1])
        well_id = y[4]
        current_timepoint = gt[gt["Timepoint"] == timepoint]

        for k, v in current_timepoint["ObjectTrackID"].items():
            obj_id = v
            x = int(current_timepoint["leftCornerX"][k])
            y = int(current_timepoint["leftCornerY"][k])
            w = int(current_timepoint["width"][k])
            h = int(current_timepoint["height"][k])
            
            image = cv2.rectangle(img, (x, y), ((x+w), (y+h)), color = (255, 0, 0), thickness=3)
            image = cv2.putText(image, str(obj_id), (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 3)
            save_image = os.path.join(RESULT_SAVE_PATH, img_name)
            cv2.imwrite(save_image, image)

