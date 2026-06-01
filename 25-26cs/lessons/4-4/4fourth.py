import random

def main():
    roll = input("Enter your input (R, Q): ")

    if roll == "R":
        return random.randint(1, 6)
    elif roll == "Q":
        quit()
    else:
        print("Invalid value, please try again.")
        return main()

def game():
    first = main()
    print(f"First number: {first}\n")

    second = main()
    times = 0
    while first != second:
        print(f"You rolled a {second}. Keep rolling!")
        times += 1
        second = main()

    print(f"\nYou rolled a {second} which matches {first}! This took you {times} rolls.\n")

    again = input("Play again? (Y, N): ")
    if again == "Y":
        game()
    elif again == "N":
        quit()
    else:
        print("Invalid value, goodbye.")
        quit()

game()


