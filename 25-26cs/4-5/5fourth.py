rows = int(input("Enter the amount of rows: "))
columns = int(input("Enter the amount of columns: "))

for i in range(1, columns + 1):
    for i in range(1, rows + 1):
        print("*", end = "")

    print()
