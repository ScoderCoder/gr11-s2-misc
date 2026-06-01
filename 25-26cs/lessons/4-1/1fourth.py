first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if second > first:
    for i in range(first, second + 1):
        print(i)
elif second < first:
    for i in range(second, first - 1, -1):
        print(i)
else:
    print(first)
