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


def ft_transpose(matrix: any):
    """Flip the rows and the columns of a 2D array."""
    rows, cols, axis = matrix.shape
    matrix2 = np.zeros((cols, rows, axis), dtype=matrix.dtype)
    for i in range(rows):
        for j in range(cols):
            matrix2[j][i] = matrix[i][j]
    return matrix2


def main():
    """Resize a picture by 400x400 pixels and rotate it to the right
    using transpose method."""
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
    img = zoom_img(img, 400, 400)
    img_array = np.array(img)
    img_array = ft_transpose(img_array)
    print(f"New shape after Transpose: {img_array.shape}")
    print(img_array)
    Image.fromarray(img_array).show()


if __name__ == "__main__":
    main()
