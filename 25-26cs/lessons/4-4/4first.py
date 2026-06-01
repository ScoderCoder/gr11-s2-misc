import random

tails = 0
heads = 0

for i in range(1, 301):
    num = random.randint(1, 2) # 1 is heads, 2 is tails
    
    if num == 1:
        heads += 1
    elif num == 2:
        tails += 1

print("Heads:", heads)
print("Tails", tails)
