rang = int(input("Enter the number of rows: "))

for i in range(rang):
    for j in range(i + 1):
        print("*  ", end="")
    print()