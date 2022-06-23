import numpy as np
import cv2 as cv
import csv
from os import listdir

import colour_processing
from colour_processing import C
import colour_processing_tests
import calibration
import colour_distance
import test_calibration_classification
import experiments

# experiments.run_experiment("experiments/e1")


# Various tests
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

# First test with C2 tooth and calibration from my room, high resolution...
# # Get the directory
# dir = "images/c2_tests/"
#
# image_list = listdir(dir)
# calibrations = calibration.get_calibrations()
#
# for image in image_list:
#     image = cv.imread(dir + image)
#     means = colour_processing.mean_colour(image)
#     print(colour_distance.classify_colour(calibrations[0], means[0], C.BGR))
#     print(colour_distance.classify_colour(calibrations[1], means[1], C.HSV))
#     print(colour_distance.classify_colour(calibrations[2], means[2], C.LAB))
#     print(colour_distance.classify_colour(calibrations[3], means[3], C.YUV))
#     print()

# Csc write and read testing
# open the file in the write mode
f = open('path', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
row = ['A1', 'A2', 'A3']
writer.writerow(row)
writer.writerow(row)

# close the file
f.close()
f = open('path', newline='')
spamreader = csv.reader(f, delimiter=' ', quotechar='|')
for row in spamreader:
    # print(', '.join(row))
    print(row)
f.close()
