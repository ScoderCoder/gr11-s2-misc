import random

first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))
total = 0
times = 0
totalavg = 0

for i in range(1, 10001):
    if first < second:
        for i in range(first, second + 1):
            rnd = random.randint(first, second)
            # print(i, rnd)
            total += rnd
            times += 1
    elif first > second:
        for i in range(second, first + 1):
            rnd = random.randint(second, first)
            # print(i, rnd)
            total += rnd
            times += 1
    elif first == second:
        print("No difference.")

    avg = round(total / times, 2)
    totalavg += avg

print(f"The average of the average sums was: {round(totalavg / 10000, 2)}")
