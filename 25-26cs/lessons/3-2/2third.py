import math

first = input("Enter first coordinate: ")
second = input("Enter second coordinate: ")

def fix(cords):
    cords = cords.replace(",", "")
    cords = cords.replace("(", "")
    cords = cords.replace(")", "")
    cords = cords.split()
    return cords

def slope(x1, y1, x2, y2):
    slopee = (y2 - y1) / (x2 - x1)
    return slopee

def distance(x1, y1, x2, y2):
    distancee = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return distancee

print(f"The distance between points {first} and {second} is {round((distance(int(fix(first)[0]), int(fix(first)[1]), int(fix(second)[0]), int(fix(second)[1]))), 3)}.")
print(f"The slope between points {first} and {second} is {round((slope(int(fix(first)[0]), int(fix(first)[1]), int(fix(second)[0]), int(fix(second)[1]))), 3)}.")

