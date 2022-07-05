def exp_to_params(i):
    # dp, minDist between centers of detected circles, higher threshold of the two passed to the Canny edge detector
    # (the lower one is twice smaller), accumulator threshold for the circle centers at the detection stage
    if i < 5:
        return [10, 20000, 30, 50, 1]
    elif i == 5:
        return [10, 20000, 30, 50, 1]
    elif i == 6:
        return [10, 20000, 30, 50, 21]
    elif i == 7:
        return [10, 20000, 30, 50, 1]
    elif i == 8:
        return [10, 20000, 30, 50, 1]
    elif i == 9:
        return [10, 20000, 20, 200, 1]
    elif i == 10:
        return [10, 20000, 20, 100, 1]
    elif i == 11:
        return [10, 20000, 30, 50, 1]
    elif i == 12:
        return [10, 20000, 30, 50, 1]
    elif i == 13:
        return [10, 20000, 40, 200, 1]
    elif i == 14:
        return [10, 20000, 20, 50, 1]
