import numpy as np


def ft_invert(array) -> np.ndarray:
    """Invert the color of a image by sustracting the maximum value of a pixel
    by the current value of the pixel"""
    return 255 - array


def ft_red(array) -> np.ndarray:
    """Making an image Red by suppressing the Green and Blue from the image."""
    array_copy = np.copy(array)
    array_copy[:, :, 1] = 0
    array_copy[:, :, 2] = 0
    return array_copy


def ft_green(array) -> np.ndarray:
    """Making an image Green by suppressing the Red and Blue from the image."""
    array_copy = np.copy(array)
    array_copy[:, :, 0] = 0
    array_copy[:, :, 2] = 0
    return array_copy


def ft_blue(array) -> np.ndarray:
    """Making an image Blue by suppressing the Red and Green from the image."""
    array_copy = np.copy(array)
    array_copy[:, :, 0] = 0
    array_copy[:, :, 1] = 0
    return array_copy


def ft_grey(array) -> np.ndarray:
    """Make an image Grey by using the standard luminosity method:
        gray = 0.299 * R + 0.587 * G + 0.114 * B"""
    array_copy = np.copy(array)
    grey = np.dot(array, [0.299, 0.587, 0.114])
    array_copy[:, :, 0] = grey
    array_copy[:, :, 1] = grey
    array_copy[:, :, 2] = grey
    return array_copy
