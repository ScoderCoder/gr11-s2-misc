first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))
total = 0

for i in range(first, second + 1):
    total += i

print(total)
