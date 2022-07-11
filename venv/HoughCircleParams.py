def exp_to_params(i):
    # dp, minDist between centers of detected circles, higher threshold of the two passed to the Canny edge detector
    # (the lower one is twice smaller), accumulator threshold for the circle centers at the detection stage

    # First case for gadget testing
    # if i == -1:
    #     return [10, 20000, 20, 50, 11]

    # First case for gadget testing
    if i == -1:
        return [10, 20000, 10, 30, 1]
    # Red tests
    elif i == -2:
        return [10, 20000, 20, 50, 11]
    elif i == -3:
        return [10, 20000, 20, 50, 11]
    elif i == -4:
        return [10, 20000, 10, 30, 1]
    elif i == 1:
        return [10, 20000, 30, 50, 1]
    elif i == 2:
        return [10, 20000, 30, 50, 1]
    elif i == 3:
        return [10, 20000, 30, 50, 1]
    elif i == 4:
        return [10, 20000, 40, 50, 11]
    elif i == 5:
        return [10, 20000, 30, 50, 11]
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
    elif i == 15:
        return [10, 20000, 20, 50, 1]
    elif i == 16:
        return [10, 20000, 20, 50, 1]
    elif i == 17:
        return [10, 20000, 20, 50, 1]
    elif i == 18:
        return [10, 20000, 20, 50, 1]
    elif i == 19:
        return [10, 20000, 20, 50, 1]
    elif i == 20:
        return [10, 20000, 20, 50, 1]
    elif i == 21:
        return [10, 20000, 20, 50, 1]
    elif i == 22:
        return [10, 20000, 20, 50, 1]
    elif i == 23:
        return [10, 20000, 20, 50, 1]
    elif i == 24:
        return [10, 20000, 20, 50, 21]
    elif i == 25:
        return [10, 20000, 20, 50, 1]
    elif i == 26:
        return [10, 20000, 20, 50, 1]
