import cv2 as cv
import csv
from os import listdir
from itertools import combinations

import colour_processing
import colour_distance
from colour_processing import C

IM_NUM = 5


def calc_means(dir):
    # Iterate over the images in the dir
    image_names = listdir(dir)

    bgr_m = []
    hsv_m = []
    lab_m = []
    yuv_m = []

    for image_name in image_names:
        image = cv.imread(dir + "/" + image_name)
        means = colour_processing.mean_colour(image)

        bgr_m.append(means[0])
        hsv_m.append(means[1])
        lab_m.append(means[2])
        yuv_m.append(means[3])

    return [bgr_m, hsv_m, lab_m, yuv_m]


def calc_dist(means):
    bgr_m, hsv_m, lab_m, yuv_m = means

    bgr_a = 0
    hsv_a = 0
    lab_a = 0
    yuv_a = 0

    combinations_list = list(combinations(list(range(IM_NUM)), 2))

    for comb in combinations_list:
        dist = colour_processing.dist(bgr_m[comb[0]], bgr_m[comb[1]], C.BGR)
        bgr_a += dist

        dist = colour_processing.dist(hsv_m[comb[0]], hsv_m[comb[1]], C.HSV)
        hsv_a += dist

        dist = colour_processing.dist(lab_m[comb[0]], lab_m[comb[1]], C.LAB)
        lab_a += dist

        dist = colour_processing.dist(yuv_m[comb[0]], yuv_m[comb[1]], C.YUV)
        yuv_a += dist

    s = len(combinations_list)
    bgr_a /= s
    hsv_a /= s
    lab_a /= s
    yuv_a /= s

    return bgr_a, hsv_a, lab_a, yuv_a


def run_gadget_tests(dir):
    tooth_dirs = listdir(dir + '/tests')
    tooth_dirs.sort()

    f = open(dir + '/gadget_results.csv', "w")
    w = csv.writer(f)

    for tooth_dir in tooth_dirs:
        image_directories = listdir(dir + '/tests/' + tooth_dir)
        image_directories.sort()

        for image_directory in image_directories:
            print(calc_dist(calc_means(dir + '/tests/' + tooth_dir + '/' + image_directory)))
            w.writerow(calc_dist(calc_means(dir + '/tests/' + tooth_dir + '/' + image_directory)))

    f.close()
