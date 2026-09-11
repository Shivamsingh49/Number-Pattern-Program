# Half pyramid
num = 5
for row in range(1, num + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()


# Inverted half pyramid
num = 5
for row in range(num, 0, -1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

