import typing

import numpy as np
from numpy import sin, tan, cos, arcsin, linspace

import matplotlib.pyplot as plt

from math import pi


def plotparaxial():
    n1 = 1
    n2 = 1.5
    # inkommande ljus har a=oändligheten

    r = 0.05
    R = 0.15
    xlimits = (-r, r)
    h = linspace(xlimits[0], xlimits[1], 1000)
    a1 = h / R
    a2 = n1 / n2 * a1
    gamma = np.pi - (np.pi - a1) - a2
    f = a2 * R / gamma + R
    plt.plot(h, f, "r", label="f")
    plt.xlim(*xlimits)
    plt.legend()


def plotf():
    plotf(R, n1, n2, r)


def plotf(R, n1, n2, r):
    xlimits = (-r, r)
    h = linspace(xlimits[0], xlimits[1], 1000)
    f = calc_f(R, h, n1, n2)
    plt.plot(h, f, "r", label="f")
    plt.xlim(*xlimits)
    plt.legend()


def calc_f(R, h, n1, n2):
    a1 = arcsin(h / R)
    a2 = arcsin(n1 / n2 * sin(a1))
    gamma = 180 - (180 - a1) - a2
    f = sin(a2) * R / sin(gamma) + R
    return f


def calc_bk7(wavelength):
    a1 = 2.271176
    a2 = -9.70070e-3
    a3 = 0.0110971
    a4 = 4.6228e-5
    a5 = 1.161610e-5
    a6 = -8.28504e-7
    return np.sqrt(
        a1 + a2 * wavelength ** 2 + a3 * wavelength ** -2 + a4 * wavelength ** -4 + a5 * wavelength ** -6 + a6 * wavelength ** -8)


def plot_chromatic(R, r, h, n1, wavelenghts, wavemin, wavemax):
    xlimits = (wavemin, wavemax)
    f = calc_f(R, h, n1, calc_bk7(wavelenghts))
    plt.plot(wavelenghts, f, "r", label="f")
    plt.xlim(*xlimits)


def main():
    n1 = 1
    n2 = 1.5
    r = 0.05
    R = 0.15
    plotf(R, n1, n2, r)
    plotparaxial()
    plt.xlabel("Height (h)")
    plt.ylabel("Focus (f)")

    plt.figure()
    wavelengths = np.linspace(400 / 1000, 700 / 1000, 300)
    n = calc_bk7(wavelengths)
    print(n)
    plt.plot(wavelengths, n)

    plt.figure()
    h = 0.025
    plot_chromatic(R, r, h, n1, wavelengths, 400 / 1000, 700 / 1000)
    plt.show()


if __name__ == "__main__":
    main()
