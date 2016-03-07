import typing

import numpy as np
from numpy import sin, tan, cos, arcsin, linspace

import matplotlib.pyplot as plt

from math import pi

def graph(n1, n2):
	"""
	Plots R_s and R_p as a function of the angle of incidence as light goes
	from a material with refractive index n1, to one with refractive index n2
	"""
    xlimits = (0, pi/2)
    a1 = linspace(xlimits[0], xlimits[1], 500)
    a2 = arcsin(n1/n2 * sin(a1))

    R_s = abs(sin(a1 - a2)/sin(a1 + a2))**2
    R_p = abs(tan(a1 - a2)/tan(a1 + a2))**2

    plt.plot(a1, R_s, label="R_s")
    plt.plot(a1, R_p, label="R_p")
    plt.xlim(*xlimits)


def main():
    n1 = 1
    n2 = 1.75

    plt.style.use('ggplot')
    plt.subplot(2, 1, 1)
    graph(n1, n2)
    brewster = np.arctan(n2/n1)
    plt.plot((brewster,brewster), (0, 1), label="brewster angle")
    plt.title("Light passing from air to glass")
    plt.xlabel("angle of incidence (radians)")
    plt.ylabel("proportion reflected")
    plt.legend(loc="upper left")


    plt.subplot(2, 1, 2)
    graph(n2, n1)
    limit = np.arcsin(n1/n2)
    plt.plot((limit,limit), (0, 1), label="limit angle")
    plt.title("Light passing from glass to air")
    plt.legend()

    plt.xlabel("angle of incidence (radians)")
    plt.ylabel("proportion reflected")
    plt.show()


if __name__ == "__main__":
    main()

