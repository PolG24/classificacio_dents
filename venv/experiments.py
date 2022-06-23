import numpy as np
import cv2 as cv
from os import listdir
import colour_processing
from colour_processing import C
import colour_processing_tests
import calibration
import colour_distance
import test_calibration_classification


def run_experiment(dir):
    # Calculate the calibrations and save them in files
