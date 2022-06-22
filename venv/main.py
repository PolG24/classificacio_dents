import numpy as np
import cv2 as cv
from os import listdir
import colour_processing
import colour_processing_tests
import calibration
import colour_distance
import test_calibration_classification

# colour_processing_tests.test_mean_colour()
# colour_processing_tests.test_dist_bgr()
# colour_processing_tests.test_dist_hsv()
# colour_processing_tests.test_dist_lab()
# colour_processing_tests.test_dist_yuv()
# test_calibration_classification.test_cal_classification()

# img = cv.imread('images/A1_test.jpg')
# means = colour_processing.mean_colour(img)
# calibrations = calibration.get_calibrations()
# print(colour_distance.classify_bgr_colour(calibrations[0], means[0]))
# print(colour_distance.classify_hsv_colour(calibrations[1], means[1]))
# print(colour_distance.classify_lab_colour(calibrations[2], means[2]))
# print(colour_distance.classify_yuv_colour(calibrations[3], means[3]))

# Get the directory
dir = "images/c2_tests/"

image_list = listdir(dir)
calibrations = calibration.get_calibrations()

for image in image_list:
    image = cv.imread(dir + image)
    means = colour_processing.mean_colour(image)
    print(colour_distance.classify_bgr_colour(calibrations[0], means[0]))
    print(colour_distance.classify_hsv_colour(calibrations[1], means[1]))
    print(colour_distance.classify_lab_colour(calibrations[2], means[2]))
    print(colour_distance.classify_yuv_colour(calibrations[3], means[3]))
    print()
