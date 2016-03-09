import typing
import numpy as np
from numpy import sin, tan, cos, arcsin, linspace
import matplotlib.pyplot as plt
from math import pi


def calc_f_paraxial(R, h, n1, n2):
    """
    Calculates the focal length for the given parameters. Assumes that sin(a) = a.
    :param R: The radius of curvature for the lens
    :param h: A numpy array of height values.
    :param n1: The refractive index of the material surrounding the lens
    :param n2: The refractive index of the lens material
    :return: A numpy array of focal lengths, one for each of the heights in h
    """
    a1 = h / R
    a2 = n1 / n2 * a1
    gamma = pi - (pi - a1) - a2
    f = a2 * R / gamma + R
    return f

def calc_f(R, h, n1, n2):
    """
    Calculates the focal length for the given parameters.
    :param R: The radius of curvature for the lens
    :param h: A numpy array of height values.
    :param n1: The refractive index of the material surrounding the lens
    :param n2: The refractive index of the lens material
    :return: A numpy array of focal lengths, one for each of the heights in h
    """
    a1 = arcsin(h / R)
    a2 = arcsin(n1 / n2 * sin(a1))
    gamma = pi - (pi - a1) - a2
    f = sin(a2) * R / sin(gamma) + R
    return f


def calc_bk7(wavelength):
    """
    Calculates the refraction index for a given wavelength of light in bk7 glass
    :param wavelength: the wavelength of the light
    :return: the refraction index for the given wavelength
    """
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
    plt.plot(wavelenghts, f, label="f")
    plt.xlim(*xlimits)
    plt.title("2c) Chromatic aberration")
    plt.xlabel("wavelength (micrometers)")
    plt.ylabel("f (m)")

def plotparaxial(R, n1, n2, r):
    xlimits = (-r, r)
    h = linspace(xlimits[0], xlimits[1], 1000)
    f = calc_f_paraxial(R, h, n1, n2)
    plt.plot(h, f, label="paraxial")
    plt.xlim(*xlimits)
    plt.legend()


def plotf(R, n1, n2, r):
    xlimits = (-r, r)
    h = linspace(xlimits[0], xlimits[1], 1000)
    f = calc_f(R, h, n1, n2)
    plt.plot(h, f,  label="non-paraxial")
    plt.xlim(*xlimits)
    plt.legend()

def plot_bk7(wavelengths):
    n = calc_bk7(wavelengths)
    plt.plot(wavelengths, n)
    plt.title("2b) BK7 glass")
    plt.xlabel("wavelengths (micrometers)")
    plt.ylabel("n")
	
def main():
    n1 = 1
    n2 = 1.5
    r = 0.05
    R = 0.15
    plt.style.use('ggplot')
    plotf(R, n1, n2, r)
    plotparaxial(R, n1, n2, r)
    plt.title("2a) Paraxial Approximation")
    plt.xlabel("h (m)")
    plt.ylabel("f (m)")

    plt.figure()
    wavelengths = np.linspace(400 / 1000, 700 / 1000, 300)
    plot_bk7(wavelengths)

    plt.figure()
    h = 0.025
    plot_chromatic(R, r, h, n1, wavelengths, 400 / 1000, 700 / 1000)
    plt.show()




if __name__ == "__main__":
    main()
