from array2D import slice_me


print("Main tests :")
family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
print()


print("More tests :")
print(slice_me(None, 0, 2))
print(slice_me([[1,2],[3,4],[5,6]], "b", 2))
print(slice_me([[1,2],[3,4],[5,6]], -1, 3))
