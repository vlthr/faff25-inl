import typing
import numpy as np
from numpy import sin, tan, cos, arcsin, linspace
import matplotlib.pyplot as plt
from math import pi


def beta(b, wavelength, x, l):
    return np.pi * b * (x / np.sqrt(x ** 2 + l ** 2)) / wavelength


def fraunhofer(b, wavelength, x, l):
    """
    Calculates the light intensity of each point in x, according to a fraunhofer model
    :param b: the width of the main (single) slit
    :param wavelength: the wavelength of the laser light
    :param x: numpy array of x (screen) positions to calculate intensities for
    :param l: the distance between the screen and slit
    :return: a numpy array of light intensities for each position in x
    """
    return (sin(beta(b, wavelength, x, l)) / beta(b, wavelength, x, l)) ** 2


def fresnel(b, N, wavelength, x, l):
    """
    Calculates the light intensity of each point in x, according to a simple fresnel model.
    :param b: the width of the main (single) slit
    :param N: the number of slits to divide the main slit into
    :param wavelength: the wavelength of the laser light
    :param x: numpy array of x (screen) positions to calculate intensities for
    :param l: the distance between the screen and slit
    :return: a numpy array of light intensities for each position in x
    """
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
    L = [1, 0.1, 0.005, 0.0025]
    x = [np.linspace(-0.02 * i, 0.02 * i, 1000) for i in L]
    frauns = [fraunhofer(b, wavelength, x[index], l) for index, l in enumerate(L)]
    fresnels = [fresnel(b, N, wavelength, x[index], l) for index, l in enumerate(L)]
    print([frauns[i] - fresnels[i] for i in range(4)])

    plt.style.use('ggplot')
    for i, l in enumerate(L):
        plt.subplot(2, 2, i + 1)
        plt.plot(x[i], frauns[i],label="fraunhofer")
        plt.plot(x[i], fresnels[i], label="fresnel")
        plt.title("l="+str(l)+" m")
        plt.xlabel("x")
        plt.ylabel("intensity")
        plt.axis([x[i][0], x[i][-1], 0, 1])
        plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
