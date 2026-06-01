sent = input("Please enter a sentence: ")
timesin = 0
printed = 0
spaceless = ""
evenstr = ""
oddstr = ""

# LEVEL 2
for i in sent:
    print(f"{i}({timesin})", end = " ")
    timesin += 1

# LEVEL 3
print("\n\nSpaces are at locations:", end = " ")

for i in range(0, len(sent)):
    if sent[i] == " ":
        print(i, end = " ")

# LEVEL 4
for i in sent:
    if i != " ":
        spaceless += i
    elif i == " ":
        spaceless += "mouse"

print(f"\n\n{spaceless}\n")

# LEVEL 4+
for i in range(0, len(spaceless)):
    if i % 2 == 0:
        evenstr += spaceless[i]
    elif i % 2 != 0:
        oddstr += spaceless[i]

print(f"Even string is: {evenstr}")
print(f"Odd string is: {oddstr}")
