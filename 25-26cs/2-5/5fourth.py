#!/usr/bin/python

# 10/02/2026
# Sougato

# Gain input
item1 = str(input("Enter first item: "))
price1 = float(input(f"Enter {item1}'s price ($): "))

item2 = str(input("Enter second item: "))
price2 = float(input(f"Enter {item2}'s price ($): "))

item3 = str(input("Enter third item: "))
price3 = float(input(f"Enter {item3}'s price ($): "))

items = [item1, item2, item3] # Putting items in a list to loop through later
prices = [price1, price2, price3] # Putting prices in a list to loop through later

# Title
print("TAB Gift Shop Receipt\n----------------")

# Loop to print
for i in range(0, 2 + 1):
    print("%-10s %6.2f" % (items[i], prices[i]))

# Find HST
hst = round((sum(prices) * 0.13), 2)

# Print HST, total
print(f"----------------\n%-10s %6.2f" % ("HST (13%)", hst))
print(f"----------------\n%-10s %6.2f" % ("Total", (sum(prices) + hst)))
