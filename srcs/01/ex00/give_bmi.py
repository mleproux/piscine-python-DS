import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if (height == None or weight == None or len(height) != len(weight)):
        return None
    if not (all(x is int or float for x in height) or all(x is int or float for x in weight)):
        return None
    height, weight = np.array(height), np.array(weight)
    bmi = weight / (height ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if bmi == None or len(bmi) == 0:
        return None
    if not (all(x is int or float for x in bmi)):
        return None
    bmi = np.array(bmi)
    filter_arr = bmi > limit
    bmi[filter_arr]
    return filter_arr.tolist()
    