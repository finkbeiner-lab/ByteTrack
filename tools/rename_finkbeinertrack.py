import os
import pdb
import glob
import cv2
import pandas as pd
from skimage import io
import numpy as np
from skimage.draw import rectangle

# Rename files to 00001.tif, where 1 denotes the current timepoint


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

    well_images = sorted(well_images)

    for well_image in well_images:
        
        # read image as it is ( 16bit format)
        img_name = os.path.basename(well_image)
        dir_name = os.path.dirname(well_image)

        y = img_name.split("_")
        timepoint = int(y[2][1])

        new_file_name = "{:05d}.tif".format(timepoint)
        dst = os.path.join(dir_name, new_file_name)

        os.rename(well_image, dst)

      