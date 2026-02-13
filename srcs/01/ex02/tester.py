from load_image import ft_load
# print(ft_load("landscape.jpg"))

try:
    print(ft_load("donttexist.jpg"))
except AssertionError as error:
    print(AssertionError.__name__ + ":", error)
    
try:
    print(ft_load(None))
except AssertionError as error:
    print(AssertionError.__name__ + ":", error)
    
try:
    print(ft_load("landscape.png"))
except AssertionError as error:
    print(AssertionError.__name__ + ":", error)