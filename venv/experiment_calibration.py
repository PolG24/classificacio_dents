import os

import numpy as np
import cv2 as cv
import colour_processing
from os import listdir


def calculate_calibrations(dir):
    image_list = listdir(dir + "/calibration_images")
    image_list.sort()

    bgr_cal = []
    hsv_cal = []
    lab_cal = []
    yuv_cal = []

    for image in image_list:
        image = cv.imread(dir + '/calibration_images/' + image)
        means = colour_processing.mean_colour(image)

        bgr_cal.append(means[0])
        hsv_cal.append(means[1])
        lab_cal.append(means[2])
        yuv_cal.append(means[3])

    # Create files and write these means in them
    if not os.path.exists(dir + "/calibration_files"):
        os.mkdir(dir + "/calibration_files")
    f_bgr = open(dir + "/calibration_files/bgr_calibrations.txt", "w")
    f_hsv = open(dir + "/calibration_files/hsv_calibrations.txt", "w")
    f_lab = open(dir + "/calibration_files/lab_calibrations.txt", "w")
    f_yuv = open(dir + "/calibration_files/yuv_calibrations.txt", "w")

    for i in range(len(bgr_cal)):
        for j in range(3):
            f_bgr.write(str(bgr_cal[i][j]) + "\n")
            f_hsv.write(str(hsv_cal[i][j]) + "\n")
            f_lab.write(str(lab_cal[i][j]) + "\n")
            f_yuv.write(str(yuv_cal[i][j]) + "\n")

    f_bgr.close()
    f_hsv.close()
    f_lab.close()
    f_yuv.close()


# Obtain the calibrations from the files
def get_calibrations(dir):
    # Create files and write these means in them
    f_bgr = open(dir + "/calibration_files/bgr_calibrations.txt", "r")
    f_hsv = open(dir + "/calibration_files/hsv_calibrations.txt", "r")
    f_lab = open(dir + "/calibration_files/lab_calibrations.txt", "r")
    f_yuv = open(dir + "/calibration_files/yuv_calibrations.txt", "r")

    bgr_cal = []
    hsv_cal = []
    lab_cal = []
    yuv_cal = []

    for i in range(16):
        bgr_cal.append([float(f_bgr.readline()[:-1]), float(f_bgr.readline()[:-1]), float(f_bgr.readline()[:-1])])
        hsv_cal.append([float(f_hsv.readline()[:-1]), float(f_hsv.readline()[:-1]), float(f_hsv.readline()[:-1])])
        lab_cal.append([float(f_lab.readline()[:-1]), float(f_lab.readline()[:-1]), float(f_lab.readline()[:-1])])
        yuv_cal.append([float(f_yuv.readline()[:-1]), float(f_yuv.readline()[:-1]), float(f_yuv.readline()[:-1])])

    f_bgr.close()
    f_hsv.close()
    f_lab.close()
    f_yuv.close()

    return [bgr_cal, hsv_cal, lab_cal, yuv_cal]
