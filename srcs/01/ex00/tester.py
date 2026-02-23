from give_bmi import give_bmi, apply_limit


print("Main tests :")
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print()

# test

print("More tests :")
empty = give_bmi(None, None)
print(empty)
print(apply_limit(empty, float("NaN")))
