# Reverse Half Pyramid
num = 5
for row in range(1, num + 1):
    for col in range(row, 0, -1):
        print(col, end=" ")
    print()


# Inverted Reverse Half Pyramid
num = 5
for row in range(num, 0, -1):
    for col in range(row, 0, -1):
        print(col, end=" ")
    print()


