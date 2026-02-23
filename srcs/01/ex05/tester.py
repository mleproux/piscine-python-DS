from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
from PIL import Image

array = ft_load("ghosttrick.jpg")

array = ft_invert(array)
array = ft_red(array)
array = ft_green(array)
array = ft_blue(array)
array = ft_grey(array)

img = Image.fromarray(array)
img.show()
