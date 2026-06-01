inp = input("Enter a string: ")
full = ""
fuller = ""

for i in range(0, len(inp)):
    if i % 2 == 0:
        full += inp[i].capitalize()
    else:
        full += inp[i]

for i in full:
    if i == " ":
        fuller += "Mr.K"
    else:
        fuller += i

print(fuller)

