import typing

import numpy as np
from numpy import sin, tan, cos, arcsin, linspace
from scipy.ndimage.interpolation import shift

import matplotlib.pyplot as plt

from math import pi


def beta(b, wavelength, x, l):
    return np.pi * b * (x / np.sqrt(x ** 2 + l ** 2)) / wavelength


def fraunhofer(b, wavelength, x, l):
    return (sin(beta(b, wavelength, x, l)) / beta(b, wavelength, x, l)) ** 2


def fresnel(b, N, wavelength, x, l):
    d = b / N
    total = np.zeros_like(x, dtype=np.complex64)
    def complexContribution(xPoint, i):
        hypot = np.sqrt(l**2 + (abs(xPoint)+i*d)**2)
        phase = 2*pi * (hypot%wavelength)/wavelength
        complexContr = np.exp(phase * 1j)
        return  complexContr
    for xIndex, xPoint in enumerate(x):
        for i in range(-N // 2, N // 2):
            total[xIndex] += complexContribution(xPoint, i)/N
    return np.abs(total)


def main():
    wavelength = 632e-9
    N = 100
    b = 100e-6
    L = [1, 0.1, 0.01, 0.001]
    x = [np.linspace(-0.02 * i, 0.02 * i, 1000) for i in L]
    frauns = [fraunhofer(b, wavelength, x[index], l) for index, l in enumerate(L)]
    fresnels = [fresnel(b, N, wavelength, x[index], l) for index, l in enumerate(L)]
    print([frauns[i] - fresnels[i] for i in range(4)])

    for index, i in enumerate(frauns):
        plt.subplot(2, 2, index + 1)
        plt.plot(x[index], frauns[index],label="fraunhofer", color="r")
        plt.plot(x[index], fresnels[index], label="fresnel", color="b")
        # plt.clabel("l=", l)
        plt.xlabel("x")
        plt.ylabel("intensity")
        plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
