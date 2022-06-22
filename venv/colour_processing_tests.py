import numpy as np
import cv2 as cv
import colour_processing

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
            abs(colour_processing.dist_bgr([42, 245, 255], [123, 44, 98]) - 267.6023) < 0.1 and
            abs(colour_processing.dist_bgr([98, 99, 100], [100, 99, 98]) - 2.8284) < 0.1 and
            abs(colour_processing.dist_bgr([234, 23, 4], [222, 1, 0]) - 25.3772) < 0.1):
        print('dist_bgr working correctly')
    else:
        print('dist_bgr not working correctly')


def test_dist_hsv():
    if (abs(colour_processing.dist_hsv([1, 2, 2], [150, 49, 255]) - 259.1891) < 0.1 and
            abs(colour_processing.dist_hsv([19, 123, 43], [45, 243, 49]) - 122.9309) < 0.1):
        print('dist_hsv working correctly')
    else:
        print('dist_hsv not working correctly')


# De moment confio que el codi que he trobat per aquest algorisme funcioni bé
def test_dist_lab():
    print(colour_processing.delta_E_CIE2000([255, 255, 255], [31, 145, 222]))


def test_dist_yuv():
    if (colour_processing.dist_bgr([1, 1, 1], [1, 1, 1]) == 0 and
            abs(colour_processing.dist_bgr([42, 245, 255], [123, 44, 98]) - 267.6023) < 0.1 and
            abs(colour_processing.dist_bgr([98, 99, 100], [100, 99, 98]) - 2.8284) < 0.1 and
            abs(colour_processing.dist_bgr([234, 23, 4], [222, 1, 0]) - 25.3772) < 0.1):
        print('dist_yuv working correctly')
    else:
        print('dist_yuv not working correctly')
