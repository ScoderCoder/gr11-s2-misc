string = input("Enter a string: ")

def howmany(string):
    times = 0

    for i in string:
        if i == "A" or i == "B" or i == "C" or i == "D" or i == "E":
            times += 1

    return times

print(f"There were {howmany(string)} occurrences of A, B, C, D or E.")
