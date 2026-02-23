import numpy as np
from PIL import Image
from load_image import ft_load


def zoom_img(img: any, x, y) -> any:
    """Crop the image using lesser dimension."""
    width = img.size[0]
    height = img.size[1]
    cx = width / 2
    cy = height / 2
    x /= 2
    y /= 2
    coords = (cx - x, cy - y, cx + x, cy + y)
    return img.crop(coords)


def main():
    """Load a image and \"zoom it\" by resizing the image
    using lesser dimension"""
    try:
        new_width = int(input("Please provide the new width in pixels:"))
        new_height = int(input("Please provide the new height in pixels:"))
        img_array = ft_load("water.jpg")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(1)
    if new_width > img_array.shape[0] or new_height > img_array.shape[0]:
        print("Error: Provided dimension are bigger than the image :")
        print(f"Image({img_array.shape[0]},{img_array.shape[1]})")
        print(f"Input({new_width},{new_height})")
        exit(1)
    print(img_array)
    img = Image.fromarray(img_array)
    img = zoom_img(img, new_width, new_height)
    img_array = np.array(img)
    print(f"New shape afting slicing : {img_array.shape}")
    print(img_array)
    img.show()


if __name__ == "__main__":
    main()
