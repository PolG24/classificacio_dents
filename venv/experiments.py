import numpy as np
import cv2 as cv
import csv
import os
from os import listdir

import experiment_calibration
import colour_processing
import colour_distance
from colour_processing import C


def calculate_results(dir, exp):
    # Calculate the calibrations and save them in files
    experiment_calibration.calculate_calibrations(dir, exp)
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
            means = colour_processing.mean_colour(image, exp)

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


EXP_IMAGES = 3
CAL_IMAGES = 16


def calculate_stats(dir):
    # Open the result files
    bgr_res_f = open(dir + "/results/bgr_results.csv", newline='')
    hsv_res_f = open(dir + "/results/hsv_results.csv", newline='')
    lab_res_f = open(dir + "/results/lab_results.csv", newline='')
    yuv_res_f = open(dir + "/results/yuv_results.csv", newline='')

    # Create the csv readers
    bgr_r = csv.reader(bgr_res_f, delimiter=',')
    hsv_r = csv.reader(hsv_res_f, delimiter=',')
    lab_r = csv.reader(lab_res_f, delimiter=',')
    yuv_r = csv.reader(yuv_res_f, delimiter=',')

    # Count the correct guesses
    correct_bgr_guesses = 0
    correct_hsv_guesses = 0
    correct_lab_guesses = 0
    correct_yuv_guesses = 0
    for tooth_i in range(CAL_IMAGES):
        for i in range(EXP_IMAGES):
            bgr_row = next(bgr_r)
            hsv_row = next(hsv_r)
            lab_row = next(lab_r)
            yuv_row = next(yuv_r)

            if int(bgr_row[0]) == tooth_i:
                correct_bgr_guesses += 1

            if int(hsv_row[0]) == tooth_i:
                correct_hsv_guesses += 1

            if int(lab_row[0]) == tooth_i:
                correct_lab_guesses += 1

            if int(yuv_row[0]) == tooth_i:
                correct_yuv_guesses += 1

    bgr_ratio = correct_bgr_guesses / (EXP_IMAGES * CAL_IMAGES)
    hsv_ratio = correct_hsv_guesses / (EXP_IMAGES * CAL_IMAGES)
    lab_ratio = correct_lab_guesses / (EXP_IMAGES * CAL_IMAGES)
    yuv_ratio = correct_yuv_guesses / (EXP_IMAGES * CAL_IMAGES)

    # Create stat file to save the results
    if not os.path.exists(dir + "/statistics"):
        os.mkdir(dir + "/statistics")
    f = open(dir + "/statistics/ratios.csv", "w")

    # Create csv writer
    w = csv.writer(f)

    w.writerow([bgr_ratio, hsv_ratio, lab_ratio, yuv_ratio])

    bgr_res_f.close()
    hsv_res_f.close()
    lab_res_f.close()
    yuv_res_f.close()

    f.close()


def join_ratios(dir, i):
    f = open(dir + '/all_stats.csv', 'w')
    w = csv.writer(f)

    for j in range(1, i + 1):
        exp_folder = dir + '/e' + str(j)

        # Open the ratio file
        ratios_f = open(exp_folder + "/statistics/ratios.csv", newline='')

        # Create the csv reader
        ratios_r = csv.reader(ratios_f, delimiter=',')

        w.writerow(next(ratios_r))

        ratios_f.close()

    f.close()


def run_experiment(dir, exp):
    calculate_results(dir, exp)
    calculate_stats(dir)


def org_exp_im(dir):
    # Iterate over the images in order
    image_names = listdir(dir)
    image_names.sort()

    for tooth_i in range(CAL_IMAGES):
        # Create image directory
        if not os.path.exists(dir + "/" + str(tooth_i)):
            os.mkdir(dir + "/" + str(tooth_i))

        for image_i in range(EXP_IMAGES):
            os.rename(dir + "/" + image_names[tooth_i * EXP_IMAGES + image_i], dir + "/" + str(tooth_i) + "/" +
                      image_names[tooth_i * EXP_IMAGES + image_i])








