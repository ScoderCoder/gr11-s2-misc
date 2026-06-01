import random

months = 50
animals = random.randint(5, 20)
origanimals = animals
food = 1000

print(f"The random number is {animals}.")

def level2(times, animals, food):
    for i in range(1, times + 1):
        before = animals * 2 - origanimals
        animals *= 2
        food = food - before + 4000

        if animals > food:
            break

        print(i, animals, animals * 2 - origanimals, food)


level2(months, animals, food)
