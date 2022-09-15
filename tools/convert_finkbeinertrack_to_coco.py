import os
import numpy as np
import json
from PIL import Image
import pdb
import glob
import pandas as pd

DATA_PATH = 'datasets/FinkbeinerTrack/'
OUT_PATH = DATA_PATH + 'annotations/'
SPLITS = ['val', 'train']
DEBUG = False

wells = glob.glob(os.path.join(DATA_PATH, "*"))




if __name__ == '__main__':
    if not os.path.exists(OUT_PATH):
        os.mkdir(OUT_PATH)
    
    wells = glob.glob(os.path.join(DATA_PATH, "*"))

    for split in SPLITS:
        data_path = DATA_PATH + split
        out_path = OUT_PATH + '{}.json'.format(split)
        image_cnt = 0
        ann_cnt = 0
        video_cnt = 0

        # Each well in a plate is a sequence of images at different timepoints
        for well in wells:
            video_cnt += 1  # video sequence number.
            print(os.path.basename(well))

            out = {'images': [], 'annotations': [], 'videos': [],
            'categories': [{'id': 1, 'name': 'cells'}]}


            ann_path = os.path.join(well, "groundtruth.csv")
            anns_data = pd.read_csv(ann_path)
            well_images = glob.glob(os.path.join(well, "*tif"))

            for well_image in well_images:

                image_info = {'file_name': '{}/img1/{:06d}.jpg'.format(well, i + 1),  # image name.
                            'id': image_cnt + i + 1,  # image number in the entire training set.
                            'frame_id': i + 1 - image_range[0],  # image number in the video sequence, starting from 1.
                            'prev_image_id': image_cnt + i if i > 0 else -1,  # image number in the entire training set.
                            'next_image_id': image_cnt + i + 2 if i < num_images - 1 else -1,
                            'video_id': video_cnt,
                            'height': height, 'width': width}

            

            