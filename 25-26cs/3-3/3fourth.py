price = float(input("Enter the price of the meal ==> "))

print("McD's\nReceipt\n-------------")
print("%-10s%10s" % ("Meal", ("$" + str(round(price, 2)))))
print("                ----")
print("%-10s%10s" % ("Tax (13%)", ("$" + str(round((price * 0.13), 2)))))
print("                ----")
print("%-10s%10s" % ("Total", ("$" + str(round((price * 1.13), 2)))))
