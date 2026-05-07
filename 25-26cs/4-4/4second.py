import random

times = 0

for i in range(1, 1001):
    num = random.randint(1, 6) 
    
    if num == 5:
        times += 1

print("The die landed on 5:", times, "times.")
