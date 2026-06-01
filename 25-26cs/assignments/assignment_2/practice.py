#!/usr/bin/python

# Sougato
# 19/02/2026

# inputs
pro1 = input("Please enter the first product: ")
pri1 = float(input("Please enter the first price: "))
# taxation
tax1 = pri1 * 0.13

pro2 = input("Please enter the second product: ")
pri2 = float(input("Please enter the second price: "))
tax2 = pri2 * 0.13

pro3 = input("Please enter the third product: ")
pri3 = float(input("Please enter the third price: "))
tax3 = pri3 * 0.13

# hardcoded header
print("Product                    Price                          Tax")
# alignment printing
print("%-20s %11.2f %28.2f" % (pro1, pri1, tax1))
print("%-20s %11.2f %28.2f" % (pro2, pri2, tax2))
print("%-20s %11.2f %28.2f" % (pro3, pri3, tax3))
# hardcoded divider
print("=============================================================")
# alignment printing + calculations
print("%-20s %11.2f %28.2f" % ("Subtotal:", (pri1 + pri2 + pri3), (tax1 + tax2 + tax3)))
print("=============================================================")
print(f"Total: ${(pri1 + pri2 + pri3 + tax1 + tax2 + tax3)}")
