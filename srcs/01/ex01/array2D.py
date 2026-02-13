import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    if family == None or not isinstance(end, int) or not isinstance(start, int):
        return None
    try:
        family = np.array(family)
        print(f"My shape is : {family.shape}")
        family = family[start:end]
        print(f"My new shape is : {family.shape}")
        return family.tolist()
    except:
        return None

# check si les arguments sont bon et non vide
# transformer la liste en array
# check avec shape si la taille de l'array est bonne
# trancher l'array avec les garguments start et end [start:end]
# retourner l'array en tant que liste