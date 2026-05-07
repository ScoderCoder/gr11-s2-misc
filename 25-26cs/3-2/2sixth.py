string = input("Enter a string with an even amount of characters: ")
fieldsize = int(input("Enter a even field size: "))

dots = int((fieldsize - len(string)) / 2)

print("." * dots + string + "." * dots)
