# Python function that calculates the local minimum point of curvature (vortex)
# in a specified interval of a unimodal function.
# Simply change the maxF variable to the function
# you'd like to test and set the parameters of max_grs.
# ---WORKS ONLY FOR ONE VARIABLE FUNCTIONS----
# ---  IT IS RECOMMENDED TO  USE 'x' AS THE VARIABLE---

from matplotlib import pyplot as plt  # import module to plot the result
import numpy as np  # import module to get access to square root and linspace


target_function = lambda x: x ** 2 - 6 * x + 15  # type the function of interest here


def min_golden_search(
    func_to_min, upper: float, lower: float, tol: float = 1e-8
) -> float:
    """
    Function in python that calculates the minimum point of a function in a specified intrerval
     f: the function to minimize
     u: upper boundary of interval
     l: lower boundary of interval
     tol: set an appropriate tolerance value
     return: minimum of specified interval
    >>> min_golden_search(target_function, 3, 4)
    count = 39
    3.000000049300109
    """

    if type(upper) is str or type(lower) is str:
        raise ValueError("Please give numerical values for upper, lower limits")
    else:

        gr = (np.sqrt(5) + 1) * 0.5  # The golden ratio number ~ 1.618
        d = (upper - lower) / gr  # Sets initial value for d

        m1 = lower + d  # Sets initial value for m1
        m2 = upper - d  # and m2

        count = 0  # Creates a count variable with initial value zero

        while (
            abs(upper - lower) > tol
        ):  # Sets the tolerance condition. Will stop running once |u -l| < tol

            if func_to_min(m1) < func_to_min(m2):  # Checks for 1st or 2nd case
                lower = m2  # Sets lower boundary to m2
            else:
                upper = m1  # Sets upper boundary to m1
            d = (upper - lower) / gr  # Calculates new d
            m1 = lower + d  # Calculates new m1
            m2 = upper - d  # Calculates new m2

            count += 1  # Adds one to the count per iteration

        print("count =", count)  # Prints the count number

        return (
            m1 + m2
        ) * 0.5  # Returns the midpoint of the final interval as the minimum point in the range


min = min_golden_search(target_function, 3, 4)

print(min)  # TODO: delete


def plot_point(
    min_point: float = min,
    x_axis_linspace: np.linspace = np.linspace(-5, 5, 200),
) -> None:
    """
    Plots function and maximum point
    """
    fmt = "bo"  # format string for the color of the point
    plt.plot(x_axis_linspace, target_function(x_axis_linspace))
    plt.plot(min_point, target_function(min_point), fmt)
    plt.show()


if __name__ == "__main__":

    import doctest

    doctest.testmod()


"""
# References

https://en.wikipedia.org/wiki/Golden-section_search

"""
