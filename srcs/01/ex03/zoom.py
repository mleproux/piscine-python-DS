import numpy as np
from PIL import Image
from load_image import ft_load


def zoom_img(img: any, x, y) -> any:
    width = img.size[0]
    height = img.size[1]
    
    cx = width / 2
    cy = height / 2
    x /= 2
    y /= 2
    coords = (cx - x, cy - y, cx + x, cy + y)
    return img.crop(coords)


def main():
    try:
        img_array = ft_load("water.jpg")
        print(img_array)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(1)
    img = Image.fromarray(img_array)
    img = zoom_img(img, 400, 400)
    img_array = np.array(img)
    print(f"New shape afting slicing : {img_array.shape}")
    print(img_array)
    img.show()


if __name__ == "__main__":
    main()
