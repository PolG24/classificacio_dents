import numpy as np
import cv2 as cv
import colour_processing
import colour_processing_tests
import calibration
import colour_distance


def test_cal_classification():
    calibrations = calibration.get_calibrations()

    for i in range(len(calibrations[0])):
        print(colour_distance.classify_bgr_colour(calibrations[0], calibrations[0][i]))

    print()

    for i in range(len(calibrations[1])):
        print(colour_distance.classify_hsv_colour(calibrations[1], calibrations[1][i]))

    print()

    for i in range(len(calibrations[2])):
        print(colour_distance.classify_lab_colour(calibrations[2], calibrations[2][i]))

    print()

    for i in range(len(calibrations[3])):
        print(colour_distance.classify_yuv_colour(calibrations[3], calibrations[3][i]))