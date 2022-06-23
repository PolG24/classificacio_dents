import numpy as np
import cv2 as cv
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

    for i, d in enumerate(image_directories):
        # Iterate over the images in the directory
        image_names = listdir(dir + "/sample_images/" + d)
        print("\n" + colour_distance.vita_from_index(i))

        bgr_clas = []
        hsv_clas = []
        lab_clas = []
        yuv_clas = []

        for image_name in image_names:
            image = cv.imread(dir + "/sample_images/" + d + "/" + image_name)
            means = colour_processing.mean_colour(image)
            bgr_clas.append(colour_distance.classify_colour(calibrations[0], means[0], C.BGR))
            hsv_clas.append(colour_distance.classify_colour(calibrations[1], means[1], C.HSV))
            lab_clas.append(colour_distance.classify_colour(calibrations[2], means[2], C.LAB))
            yuv_clas.append(colour_distance.classify_colour(calibrations[3], means[3], C.YUV))

        print("BGR:")
        for clas in bgr_clas:
            print(clas)

        print("HSV:")
        for clas in hsv_clas:
            print(clas)

        print("LAB:")
        for clas in lab_clas:
            print(clas)

        print("YUV:")
        for clas in yuv_clas:
            print(clas)
