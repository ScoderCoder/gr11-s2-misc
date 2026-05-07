ask = input("Enter a string: ")
asklist = list(ask)
askrlist = list(ask)
askrlist.reverse()

for i in range(0, len(askrlist)):
    print(f"{asklist[i]}\t{askrlist[i]}")

