from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
from PIL import Image

array = ft_load("ghosttrick.jpg")
array = ft_grey(array)

# ft_red(array)
# ft_green(array)
# ft_blue(array)
# ft_grey(array)
# print(ft_invert.__doc__)

img = Image.fromarray(array)
img.show()