#!/usr/bin/python

# 11/02/2026
# Sougato

# gain input
number = int(input("Enter your number: "))

# one line
xline = "x" * number

# loop
for i in range(1, number+1):
    print(xline)


print("--")

# no loop
print((xline + "\n") * number)
