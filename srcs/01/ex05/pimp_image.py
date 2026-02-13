import numpy as np

def ft_invert(array) -> np.ndarray:
    return 255 - array


def ft_red(array) -> np.ndarray:
    array_copy = np.copy(array)
    
    array_copy[:, :, 1] = 0
    array_copy[:, :, 2] = 0
    
    return array_copy

def ft_green(array) -> np.ndarray:
    array_copy = np.copy(array)
    
    array_copy[:, :, 0] = 0
    array_copy[:, :, 2] = 0
    
    return array_copy


def ft_blue(array) -> np.ndarray:
    array_copy = np.copy(array)
    
    array_copy[:, :, 0] = 0
    array_copy[:, :, 1] = 0
    
    return array_copy


def ft_grey(array) -> np.ndarray:
    array_copy = np.copy(array)
    gray = np.dot(array, [0.299, 0.587, 0.114])
    
    array_copy[:, :, 0] = gray
    array_copy[:, :, 1] = gray
    array_copy[:, :, 2] = gray
    
    return array_copy