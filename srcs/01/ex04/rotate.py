import numpy as np
from PIL import Image
from load_image import ft_load

def ft_transpose(matrix: any):
    rows, cols, axis = matrix.shape
    matrix2 = np.zeros((cols, rows, axis), dtype=matrix.dtype)
    
    for i in range(rows):
        for j in range(cols):
            matrix2[j][i] = matrix[i][j]
    return matrix2

def main():
    try:
        img_array = ft_load("water.jpg")
        print(img_array)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(1)
    img_array = ft_transpose(img_array)
    img = Image.fromarray(img_array)
    print(f"New shape after Transpose: {img_array.shape}")
    print(img_array)
    img.show()


if __name__ == "__main__":
    main()
