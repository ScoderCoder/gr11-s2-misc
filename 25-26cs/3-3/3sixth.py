length = float(input("Please enter the the length of your python: "))
origlength = length

needed = 0

if length >= 6:
    length -= 6
    needed += 6 * 0.5
    needed += length * 0.75
elif length < 6:
    needed += length * 0.5 

print(f"A {origlength}' python needs {round(needed, 2)} square feet.")
