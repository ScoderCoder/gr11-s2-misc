length = int(input("Enter rectangle length: "))
width = int(input("Enter rectangle width: "))

area = length * width
perimeter = (2 * length) + (2 * width)

if area > perimeter:
    print("The area of the rectangle is greater than the perimeter.")
elif area == perimeter:
    print("The area of the rectangle is equal to the perimeter.")
elif area < perimeter:
    print("The area of the rectangle is less than the perimeter")
