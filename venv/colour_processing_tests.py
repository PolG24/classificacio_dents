import numpy as np
import cv2 as cv
import colour_processing
from colour_processing import C

# cv.imshow('i', img_bgr)
# cv.waitKey(0)
# cv.destroyAllWindows()


def test_mean_colour():
    image = cv.imread('images/dent.jpg')
    means = colour_processing.mean_colour(image)

    # Tests to see the means generated make sense and are approximately the same when rewritten in BGR
    # Transform each mean into a one-pixel image
    for i in range(len(means)):
        means[i] = np.array([[[int(means[i][0]), int(means[i][1]), int(means[i][2])]]], dtype=np.uint8)

    bgr_mean, hsv_mean, lab_mean, yuv_mean = means

    print('BGR: ' + str(bgr_mean))
    print('HSV: ' + str(hsv_mean))
    print('LAB: ' + str(lab_mean))
    print('YUV: ' + str(yuv_mean) + '\n')

    print(means[0])

    hsv2bgr_mean = cv.cvtColor(hsv_mean, cv.COLOR_HSV2BGR)
    print(hsv2bgr_mean)
    lab2bgr_mean = cv.cvtColor(lab_mean, cv.COLOR_LAB2BGR)
    print(lab2bgr_mean)
    yuv2bgr_mean = cv.cvtColor(yuv_mean, cv.COLOR_YUV2BGR)
    print(yuv2bgr_mean)
    print('\n')


def test_dist_bgr():
    if (colour_processing.dist_bgr([1, 1, 1], [1, 1, 1]) == 0 and
            abs(colour_processing.dist([42, 245, 255], [123, 44, 98], C.BGR) - 267.6023) < 0.1 and
            abs(colour_processing.dist([98, 99, 100], [100, 99, 98], C.BGR) - 2.8284) < 0.1 and
            abs(colour_processing.dist([234, 23, 4], [222, 1, 0], C.BGR) - 25.3772) < 0.1):
        print('dist_bgr working correctly')
    else:
        print('dist_bgr not working correctly')


def test_dist_hsv():
    if (abs(colour_processing.dist([1, 2, 2], [150, 49, 255], C.HSV) - 259.1891) < 0.1 and
            abs(colour_processing.dist([19, 123, 43], [45, 243, 49], C.HSV) - 122.9309) < 0.1):
        print('dist_hsv working correctly')
    else:
        print('dist_hsv not working correctly')


# De moment confio que el codi que he trobat per aquest algorisme funcioni bé
def test_dist_lab():
    print(colour_processing.dist([255, 255, 255], [31, 145, 222], C.LAB))


def test_dist_yuv():
    if (colour_processing.dist([1, 1, 1], [1, 1, 1], C.YUV) == 0 and
            abs(colour_processing.dist([42, 245, 255], [123, 44, 98], C.YUV) - 267.6023) < 0.1 and
            abs(colour_processing.dist([98, 99, 100], [100, 99, 98], C.YUV) - 2.8284) < 0.1 and
            abs(colour_processing.dist([234, 23, 4], [222, 1, 0], C.YUV) - 25.3772) < 0.1):
        print('dist_yuv working correctly')
    else:
        print('dist_yuv not working correctly')
