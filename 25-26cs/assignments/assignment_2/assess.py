#!/usr/bin/python

# Sougato
# 20/02/2026

# INPUTS
agent1 = input("Please enter the first agent: ")
# F STRING PRICE
price1 = int(input(f"Please enter the sale price for agent {agent1}: "))
# CALCULATION
com1 = price1 * 0.025

agent2 = input("Please enter the second agent: ")
price2 = int(input(f"Please enter the sale price for agent {agent2}: "))
com2 = price2 * 0.025

agent3 = input("Please enter the third agent: ")
price3 = int(input(f"Please enter the sale price for agent {agent3}: "))
com3 = price3 * 0.025

# HEADING
print("%-21s%11s%13s" % ("Agent", "Price", "Commission"))

# TABLE
print("%-21s%11i%13.2f" % (agent1, price1, com1))
print("%-21s%11i%13.2f" % (agent2, price2, com2))
print("%-21s%11i%13.2f" % (agent3, price3, com3))
