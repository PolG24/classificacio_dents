import numpy as np
import cv2 as cv
import colour_processing
from colour_processing import C
import colour_processing_tests
import calibration
import colour_distance


def test_cal_classification():
    calibrations = calibration.get_calibrations()

    for i in range(len(calibrations[0])):
        print(colour_distance.classify_colour(calibrations[0], calibrations[0][i], C.BGR))

    print()

    for i in range(len(calibrations[1])):
        print(colour_distance.classify_colour(calibrations[1], calibrations[1][i], C.HSV))

    print()

    for i in range(len(calibrations[2])):
        print(colour_distance.classify_colour(calibrations[2], calibrations[2][i], C.LAB))

    print()

    for i in range(len(calibrations[3])):
        print(colour_distance.classify_colour(calibrations[3], calibrations[3][i], C.YUV))