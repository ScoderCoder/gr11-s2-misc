que = int(input("How many astericks would you like to see? "))

def printStars():
    stars = "*" * 55
    return stars

def lineOfStars(amt):
    starss = "*" * amt
    return starss

print(printStars())
print(lineOfStars(que))
print(printStars())
