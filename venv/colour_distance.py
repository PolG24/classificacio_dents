import numpy as np
import cv2 as cv
import colour_processing
import calibration


def calculate_bgr_distances(calibrations, colour):
    distances = []

    for col in calibrations:
        distances.append(colour_processing.dist_bgr(col, colour))

    return distances


def calculate_hsv_distances(calibrations, colour):
    distances = []

    for col in calibrations:
        distances.append(colour_processing.dist_hsv(col, colour))

    return distances


def calculate_lab_distances(calibrations, colour):
    distances = []

    for col in calibrations:
        distances.append(colour_processing.dist_lab(col, colour))

    return distances


def calculate_yuv_distances(calibrations, colour):
    distances = []

    for col in calibrations:
        distances.append(colour_processing.dist_yuv(col, colour))

    return distances


def vita_from_index(i):
    if i == 0:
        return 'A1'
    elif i == 1:
        return 'A2'
    elif i == 2:
        return 'A3'
    elif i == 3:
        return 'A3,5'
    elif i == 4:
        return 'A4'
    elif i == 5:
        return 'B1'
    elif i == 6:
        return 'B2'
    elif i == 7:
        return 'B3'
    elif i == 8:
        return 'B4'
    elif i == 9:
        return 'C1'
    elif i == 10:
        return 'C2'
    elif i == 11:
        return 'C3'
    elif i == 12:
        return 'C4'
    elif i == 13:
        return 'D2'
    elif i == 14:
        return 'D3'
    elif i == 15:
        return 'D4'


def result_from_distances(distances):
    result = []
    for i in range(len(distances)):
        result.append((vita_from_index(i), distances[i]))

    result.sort(key=lambda x: x[1])

    return result


def classify_bgr_colour(calibrations, colour):
    return result_from_distances(calculate_bgr_distances(calibrations, colour))


def classify_hsv_colour(calibrations, colour):
    return result_from_distances(calculate_hsv_distances(calibrations, colour))


def classify_lab_colour(calibrations, colour):
    return result_from_distances(calculate_lab_distances(calibrations, colour))


def classify_yuv_colour(calibrations, colour):
    return result_from_distances(calculate_yuv_distances(calibrations, colour))
