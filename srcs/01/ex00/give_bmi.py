import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Return of the bmi value of the provided lists.
    - Return None if the values are not correct"""
    if (height is None or weight is None or len(height) != len(weight)):
        return None
    try:
        height = np.array(height, dtype='float')
        weight = np.array(weight, dtype='float')
        bmi = weight / (height ** 2)
        return bmi.tolist()
    except ValueError:
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of boolean which ckeck
    if the bmi values are below the provided limit.
    - Return None if the values are not correct"""
    if bmi is None or len(bmi) == 0:
        return None
    try:
        bmi = np.array(bmi, dtype='float')
        filter_arr = bmi > limit
        bmi[filter_arr]
        return filter_arr.tolist()
    except ValueError:
        return None
