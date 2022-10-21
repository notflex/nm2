import matplotlib.pyplot as plt
import numpy as np


def get_func(x):
    return np.cos(x) ** 2


def get_dif_func(x):
    return 2 * np.cos(x) * np.sin(x)


def get_dif2_func(x):
    return 2 * np.cos(x) ** 2 - 2 * np.sin(x) ** 2


def center(x_r, x_l, step):
    return (x_r - x_l) / (2 * step)


def d_right(x_r, x, step):
    return (x_r - x) / step


def center2(x_l, x, x_r, step):
    return (x_r - 2 * x + x_l) / step ** 2


def center4(x_l_left, x_l, x, x_r, x_r_right, step):
    return (-x_r_right + 16 * x_r - 30 * x + 16 * x_l - x_l_left) / (12 * step ** 2)


def get_errors(arr_default, arr_calculated):
    errors = []
    for i, f in enumerate(arr_default):
        errors.append(np.abs(f - arr_calculated[i]))
    return errors


if __name__ == '__main__':
    left = -1.5
    right = 1.5

    d_dif1_mid = []
    d_dif1_right = []
    d_dif2_precision2 = []
    d_dif2_precision4 = []

    startstep = 0.02
    endstep = 0.21
    deltastep = 0.02

    plt.close('all')

    for step in np.arange(startstep, endstep, deltastep):
        arr_x = np.arange(left, right, step)
        arr_x_center = arr_x[1:-1]
        arr_x_right = arr_x[:-1]
        arr_x_center2 = arr_x[1:-1]
        arr_x_center4 = arr_x[2:-2]

        func = [get_func(x) for x in arr_x]
        dif_func = [get_dif_func(x) for x in arr_x]
        dif2_func = [get_dif2_func(x) for x in arr_x]

        my_dif_func_mid = [center(func[i + 1], func[i - 1], step) for i in range(1, len(arr_x) - 1)]
        my_dif_func_right = [d_right(func[i + 1], func[i], step) for i in range(len(arr_x) - 1)]
        my_dif2_func_precision2 = [center2(func[i - 1], func[i], func[i + 1], step) for i in range(1, len(arr_x) - 1)]
        my_dif2_func_precision4 = [center4(func[i - 2], func[i - 1], func[i], func[i + 1], func[i + 2], step) for i in
                                   range(2, len(arr_x) - 2)]

        error_dif1_mid = get_errors(dif_func[1:-1], my_dif_func_mid)
        error_dif1_right = get_errors(dif_func[:-1], my_dif_func_right)
        error_dif2_precision2 = get_errors(dif2_func[1:-1], my_dif2_func_precision2)
        error_dif2_precision4 = get_errors(dif2_func[2:-2], my_dif2_func_precision4)

        d_dif1_mid.append(np.log(max(error_dif1_mid)) * 10)
        d_dif1_right.append(np.log(max(error_dif1_right)) * 10)
        d_dif2_precision2.append(np.log(max(error_dif2_precision2)) * 10)
        d_dif2_precision4.append(np.log(max(error_dif2_precision4)) * 10)

        plt.subplot(2, 2, 1)
        plt.title('dif1')
        plt.plot(arr_x, dif_func, color='b', label='default')
        plt.plot(arr_x_center, my_dif_func_mid, color='r', label='middle')
        plt.plot(arr_x_right, my_dif_func_right, color='g', label='right')
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.title('dif2')
        plt.plot(arr_x, dif2_func, color='b', label='default')
        plt.plot(arr_x_center2, my_dif2_func_precision2, color='r', label='precision2')
        plt.plot(arr_x_center4, my_dif2_func_precision4, color='g', label='precision4')
        plt.legend()

        plt.subplot(2, 2, 3)
        plt.title('dif1 errors')
        plt.plot(arr_x_center, error_dif1_mid, color='r', label='middle error')
        plt.plot(arr_x_right, error_dif1_right, color='g', label='right error')
        plt.legend()

        plt.subplot(2, 2, 4)
        plt.title('dif2 errors')
        plt.plot(arr_x_center2, error_dif2_precision2, color='r', label='precision2 error')
        plt.plot(arr_x_center4, error_dif2_precision4, color='g', label='precision4 error')
        plt.legend()

        plt.figtext(0.05, 0.95, f"step: {round(step, 2)}", color='g')
        plt.show()

    line_x = [-40, -20]
    line_y = [-40, -20]
    line_2y = [-80, -40]

    plt.subplot(2, 2, 1)
    plt.title('dif1_mid', color='r')
    plt.xlabel('10*log(h)')
    plt.ylabel('10*log(error)')
    plt.plot(10 * np.log(np.arange(startstep, endstep, deltastep)), d_dif1_mid, label='logerror')
    plt.plot(line_x, line_y, color='g')
    plt.plot(line_x, line_2y, color='g')

    plt.subplot(2, 2, 2)
    plt.title('dif1_right', color='r')
    plt.xlabel('10*log(h)')
    plt.ylabel('10*log(error)')
    plt.plot(10 * np.log(np.arange(startstep, endstep, deltastep)), d_dif1_right, label='logerror')
    plt.plot(line_x, line_y, color='g')
    plt.plot(line_x, line_2y, color='g')

    plt.subplot(2, 2, 3)
    plt.title('dif2_precision2', color='r')
    plt.xlabel('10*log(h)')
    plt.ylabel('10*log(error)')
    plt.plot(10 * np.log(np.arange(startstep, endstep, deltastep)), d_dif2_precision2, label='logerror')
    plt.plot(line_x, line_y, color='g')
    plt.plot(line_x, line_2y, color='g')

    plt.subplot(2, 2, 4)
    plt.title('dif2_precision4', color='r')
    plt.xlabel('10*log(h)')
    plt.ylabel('10*log(error)')
    plt.plot(10 * np.log(np.arange(startstep, endstep, deltastep)), d_dif2_precision4, label='logerror')
    plt.plot(line_x, line_y, color='g')
    plt.plot(line_x, line_2y, color='g')

    plt.legend()
    plt.show()
