# Python function that calculates minimum point in a specified interval of a unimodal function. Simply change the minF variable to the function you'd like to test and set the parameters of grs.
# ---WORKS ONLY FOR ONE VARIABLE FUNCTIONS----
# ---  IT IS RECOMMENDED TO  USE 'x' AS VARIABLE---

from matplotlib import pyplot as plt  # import module to plot the result
import numpy as np  # import module to get access to square root and linspace


def f(x):  # define your function that goes into parameter f here
    minF = x ** 2 - 6 * x + 15
    return minF


def grs(f, u: float, l: float, tol: float = 1e-8) -> float:
    """
    Function in python that calculates the minimum point of a function in a specified intrerval
     f: the function to minimize
     u: upper boundary of interval
     l: lower boundary of interval
     tol: set an appropriate tolerance value
     return: minimum of specified interval
    """
    if type(u) is str or type(l) is str:
        raise ValueError("Please give numerical values for upper, lower limits")
    else:

        gr = (np.sqrt(5) + 1) * 0.5  # The golden ratio number ~ 1.618
        d = (u - l) / gr  # Sets initial value for d

        m1 = l + d  # Sets initial value for m1
        m2 = u - d  # and m2
        count = 0  # Creates a count variable with initial value zero

        while (
            abs(u - l) > tol
        ):  # Sets the tolerance condition. Will stop running once |u -l| < tol

            if f(m1) < f(m2):  # Checks for 1st or 2nd case
                l = m2  # Sets lower boundary to m2
            else:
                u = m1  # Sets upper boundary to m1
            d = (u - l) / gr  # Calculates new d
            m1 = l + d  # Calculates new m1
            m2 = u - d  # Calculates new m2

            count += 1  # Adds one to the count per iteration

        print("count =", count)  # Prints the count number

        return (
            m1 + m2
        ) * 0.5  # Returns the midpoint of the final interval as the minimum point in the range


min = grs(f, 3, 4)

print(min, f(min))

x_axis = np.linspace(-5, 5, 200)

plt.plot(x_axis, f(x_axis))
plt.plot(min, f(min), "ro")
plt.show()

"""
# References

https://en.wikipedia.org/wiki/Golden-section_search

"""