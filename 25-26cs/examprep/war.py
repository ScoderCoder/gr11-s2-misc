# Sougato Chakrobortty
# 11/06/2026 Exam Preparation

import random # used by levels 3, 4+

# level 4+ (depends on level 2 & 3, modifies code in level 2, 3)

length = 1

while length % 2 != 0:
    length = random.randint(10, 100)

# level 2

numlist = []

for i in range(1, length + 1):
    numlist.append(i)

print(f"Level 2: {numlist}")

# level 3 (requires level 2)

hands = [[], []]

random.shuffle(numlist)

for i in range(2):
    for j in range(length // 2):
        hands[i].append(numlist[0])
        numlist.pop(0)

print(f"Level 3: {hands}")

# level 4 (requires level 3)

for i in range(len(hands[0])):
    print(f"Level 4, round {i}: {hands[0][i]} vs {hands[1][i]}", end = " --> ")
    
    if hands[0][i] > hands[1][i]:
        print("Hand 1 wins")
    elif hands[0][i] < hands[1][i]:
        print("Hand 2 wins")
