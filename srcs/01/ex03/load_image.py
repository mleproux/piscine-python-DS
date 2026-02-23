from PIL import Image
from PIL import UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load a jpg/jpeg file using the path parameter
    and return a numpy array of the image.
    - Return an exception is the path of file is not valid."""
    if path is None:
        raise AssertionError("Empty argument.")
    if not str.lower(path).endswith(("jpg", "jpeg")):
        raise AssertionError("Incorrect image format")
    try:
        img = Image.open(path)
    except FileNotFoundError:
        raise AssertionError(f"Image '{path}' not found.")
    except UnidentifiedImageError:
        raise AssertionError(f"File '{path}' is not a valid image.")
    img_array = np.array(img)
    print(f"My shape is : {img_array.shape}")
    return img_array
