import numpy as np
import cv2 as cv
import csv
import os
from os import listdir

import experiment_calibration
import colour_processing
import colour_distance
from colour_processing import C


def run_experiment(dir):
    # Calculate the calibrations and save them in files
    experiment_calibration.calculate_calibrations(dir)
    calibrations = experiment_calibration.get_calibrations(dir)

    # Iterate over the directories in sample images in order
    image_directories = listdir(dir + "/sample_images")
    image_directories = list(map(int, image_directories))
    image_directories.sort()
    image_directories = list(map(str, image_directories))

    # Create result files
    if not os.path.exists(dir + "/results"):
        os.mkdir(dir + "/results")
    bgr_f = open(dir + "/results/bgr_results.csv", "w")
    hsv_f = open(dir + "/results/hsv_results.csv", "w")
    lab_f = open(dir + "/results/lab_results.csv", "w")
    yuv_f = open(dir + "/results/yuv_results.csv", "w")

    # Create csv writers
    bgr_w = csv.writer(bgr_f)
    hsv_w = csv.writer(hsv_f)
    lab_w = csv.writer(lab_f)
    yuv_w = csv.writer(yuv_f)

    for i, image_dir in enumerate(image_directories):
        # Iterate over the images in the directory
        image_names = listdir(dir + "/sample_images/" + image_dir)

        for image_name in image_names:
            image = cv.imread(dir + "/sample_images/" + image_dir + "/" + image_name)
            means = colour_processing.mean_colour(image)

            row = []
            for tup in colour_distance.classify_colour(calibrations[0], means[0], C.BGR):
                row.append(tup[0])
                row.append(tup[1])

            bgr_w.writerow(row)

            row = []
            for tup in colour_distance.classify_colour(calibrations[1], means[1], C.HSV):
                row.append(tup[0])
                row.append(tup[1])

            hsv_w.writerow(row)

            row = []
            for tup in colour_distance.classify_colour(calibrations[2], means[2], C.LAB):
                row.append(tup[0])
                row.append(tup[1])

            lab_w.writerow(row)

            row = []
            for tup in colour_distance.classify_colour(calibrations[3], means[3], C.YUV):
                row.append(tup[0])
                row.append(tup[1])

            yuv_w.writerow(row)

    bgr_f.close()
    hsv_f.close()
    lab_f.close()
    yuv_f.close()
