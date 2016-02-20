import typing

import numpy as np
from numpy import sin, tan, cos, arcsin, linspace

import matplotlib.pyplot as plt

from math import pi


def graph(n1, n2):
    xlimits = (-pi/2, pi/2)
    a1 = linspace(xlimits[0], xlimits[1], 500)
    a2 = arcsin(n1/n2 * sin(a1))

    R_s = abs(sin(a1 - a2)/sin(a1 + a2))**2
    R_p = abs(tan(a1 - a2)/tan(a1 + a2))**2

    plt.plot(a1, R_s, "r")
    plt.plot(a1, R_p, "b")
    plt.xlim(*xlimits)

    #plt.axis().set_ticks(*xlimits)


def main():
    n1 = 1
    n2 = 1.75

    plt.subplot(2, 1, 1)
    graph(n1, n2)

    plt.subplot(2, 1, 2)
    graph(n2, n1)

    plt.xlabel("Radians")
    plt.show()


if __name__ == "__main__":
    main()

