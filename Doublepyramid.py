rowsize = int(input("Enter the number of rows:\n"))
number = 1
if rowsize <= 0:
    print("Please enter a positive integer.")
else:
    if rowsize%2 == 0:
        half_diamond = int(rowsize / 2)
    else:
        half_diamond = int(rowsize / 2) + 1
    space = half_diamond - 1
    for i in range(1, half_diamond + 1):
        for j in range(1, space + 1):
            print(" ", end="")
        space -= 1
        num = 1
        for j in range(2*i - 1):
            print(end=str(num))
            num += 1
        print()
    space = 1
    for i in range(1, half_diamond):
        for j in range(1, space + 1):
            print(" ", end="")
        space += 1
        num = 1
        for j in range(1, 2*(half_diamond - i)):
            print(end=str(num))
            num += 1
        print()
    print("The double pyramid is complete with", rowsize, "rows.")
