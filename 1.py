import typing

from math import sin, tan, cos
from statistics import pstdev as pstd

import numpy as np
import matplotlib.pyplot as plt


def main():
    a1 = 10
    a2 = 10

    n1 = 1
    n2 = 1.75

    R_s = abs(sin(a1 - a2)/sin(a1 + a2))**2
    R_p = abs(tan(a1 - a2)/tan(a1 + a2))**2

    x = np.linspace(0, 10, 101)
    print(x)
    y = x**2
    plt.plot(x, y, ".r")
    plt.show()


main()

