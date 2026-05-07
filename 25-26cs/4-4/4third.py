import random

times = 0

for i in range(1, 10001):
    num = random.randint(1, 2) # 1 is heads, 2 is tails
    num2 = random.randint(1, 2) # 1 is heads, 2 is tails
    
    if num == num2:
        times += 1

print("The dice were the same:", times, "times.")
