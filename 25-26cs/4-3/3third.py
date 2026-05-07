num = int(input("Enter a number between 1 and 15: "))
prod = 1

for i in range(1, num + 1):
    prod *= i

print(prod)
