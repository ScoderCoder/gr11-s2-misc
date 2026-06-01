num = input("Enter a number: ")
prod = 1

for i in num:
    if int(i) % 2 != 0:
        prod *= int(i)

print(prod)
