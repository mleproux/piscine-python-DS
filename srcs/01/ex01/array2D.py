import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Truncate an array based on the provided start and end arguments.
    - Return None if the arguments are not valid"""
    if family is None:
        return None
    if not isinstance(end, int) or not isinstance(start, int):
        return None
    family = np.array(family)
    print(f"My shape is : {family.shape}")
    family = family[start:end]
    print(f"My new shape is : {family.shape}")
    return family.tolist()
