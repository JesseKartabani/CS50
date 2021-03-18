from cs50 import get_int

# Prompt user for height of pyramid
while True:
    pyramid = get_int("Height ")
# Make sure the input is between 1 and 8
    if pyramid >= 1 and pyramid <= 8:
        break

# Create pyramid
for i in range(pyramid):
    for j in range(pyramid):
        if i + j >= pyramid - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()
    