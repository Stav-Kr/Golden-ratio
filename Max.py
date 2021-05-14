from matplotlib import pyplot as plt  # import module to plot the result
import numpy as np  # import module to get access to square root and linspace


def max_grs(f, u, l, tol=1e-8):

    """
    Function in python that calculates the maximum point in a specified interval
        f : the function to maximize
        u: upper boundary of interval
        l: lower boundary of interval
        tol: set an appropriate tolerance value
        return: maximum of specified interval
    """

    inv_gr = (np.sqrt(5) - 1) * 0.5  # ~ 0.618
    d_max = (u - l) * inv_gr # # Sets initial value for d
    q1 = l + d_max # Sets initial value for q1
    q2 = u - d_max # and q2

    count = 0 # Creates a count variable with initial value zero

    while abs(u - l) > tol: # Sets the tolerance condition. Will stop running once |u -l| < tol

        if f(q1) > f(q2):
            l = q2
        else:
            u = q1
        d_max = (u - l) * inv_gr
        q1 = l + d_max
        q2 = u - d_max
        count += 1 # Adds one to the count per iteration

    print('count =', count) # Prints the count number
    return (q1 + q2) * 0.5 # Returns the midpoint of the final interval as the maximum point in the range

def max_f(x):
    maxF = (x ** 3 - 6 * x ** 2 + 4 * x + 12)
    return maxF


maxim = max_grs(max_f, -2, 4)

print(maxim, max_f(maxim))

xx = np.linspace(-5, 5, 200)

plt.plot(xx, max_f(xx))
plt.plot(maxim, max_f(maxim), 'bo')
plt.show()