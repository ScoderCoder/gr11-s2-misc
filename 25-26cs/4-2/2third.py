age = 0
agelist = []

while age != -1:
    age = int(input("Enter the age of your family member: "))
    agelist.append(age)

agelist.pop(-1)

print(f"Average age: {round((sum(agelist) / len(agelist)), 2)}")
