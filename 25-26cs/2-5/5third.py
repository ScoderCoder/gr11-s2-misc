#!/usr/bin/python

# 10/02/2026
# Sougato

# Obtain data
name = input("Enter your name: ")

mark1 = float(input("\nEnter your first mark (out of 60): "))
mark2 = float(input("Enter your second mark (out of 60): "))
mark3 = float(input("Enter your third mark (out of 60): "))
mark4 = float(input("Enter your fourth mark (out of 60): "))
mark5 = float(input("Enter your fifth mark (out of 60): "))

# Put marks in a list, so I can index through them in a loop
marks = [mark1, mark2, mark3, mark4, mark5]

percenttotal = 0 # Variable init

# Heading
print("%-10s Percent" % (name))

# Loop starts from 0, as it is the first value in a list
# Goes up each time
for i in range(0, 4 + 1):
    percent = round(((marks[i]/60)*100), 1) # marks[i] takes that mark number and runs it through the formula to convert to percent
    print("%-10.2f %6.2f%%" % (marks[i], percent)) # print

    percenttotal = percenttotal + percent # Add each time to get average later

print(f"\nThe average percentage grade for {name} is: {round((percenttotal / 5), 1)}%.") # Average
