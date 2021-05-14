from matplotlib import pyplot as plt  # import module to plot the result

import numpy as np  # import module to get access to square root and linspace


def grs(f, u, l, tol=1e-8):
    """
    Function in python that calculates the minimum point in a specified intrerval
     f: the function to minimize
     u: upper boundary of interval
     l: lower boundary of interval
     tol: set an appropriate tolerance value
     return: minimum of specified interval
    """
    gr = (np.sqrt(5) + 1) * 0.5  # The golden ratio number ~ 1.618
    d = (u - l) / gr  # Sets initial value for d

    m1 = l + d  # Sets initial value for m1
    m2 = u - d  # and m2
    count = 0  # Creates a count variable with initial value zero

    while abs(u - l) > tol:  # Sets the tolerance condition. Will stop running once |u -l| < tol

        if f(m1) < f(m2):  # Checks for 1st or 2nd case
            l = m2  # Sets lower boundary to m2
        else:
            u = m1  # Sets upper boundary to m1
        d = (u - l) / gr  # Calculates new d
        m1 = l + d  # Calculates new m1
        m2 = u - d  # Calculates new m2

        count += 1  # Adds one to the count per iteration

    print('count =', count)  # Prints the count number

    return (m1 + m2) * 0.5  # Returns the midpoint of the final interval as the minimum point in the range


def f(x):
    tt = (x ** 2 - 6 * x + 15)
    return tt


min = grs(f, 2, 4)

print(min, f(min))

xx = np.linspace(-5, 5, 200)

plt.plot(xx, f(xx))
plt.plot(min, f(min), 'ro')
plt.show()
