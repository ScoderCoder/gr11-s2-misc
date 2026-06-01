names = []

def askname():
    nameb = input("Enter a name: ")
    return nameb

for i in range(1, 6):
    names.append(askname())

names.sort()
print(names)
