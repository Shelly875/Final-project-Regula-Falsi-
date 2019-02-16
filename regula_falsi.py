import math
def f(x):

    """
    :param x: given temp root
    :return: the value of the polynomial in x
    """

    return x ** 3 + 2 * x ** 2 + 10 * x - 20


def regula_falsi(f, x0, x1, acceptable_error):

    """
    :param f: a polynomial
    :param x0: the first x point of an interval
    :param x1: the second x point of an interval
    :param acceptable_error: the max error for stopping the calculation
    :return: the root of a given polynomial
    """

    i = 0
    x = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))

    while abs(f(x)) >= acceptable_error:
        x = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))

        if f(x) == 0:
            break
        elif f(x0) * f(x) < 0:
            x0 = x
        else:
            x1 = x
        print('Iteration ', i, ': ', x)
        i += 1
    return x


#print(regula_falsi(lambda x: x**2, -2, 2, 1))




