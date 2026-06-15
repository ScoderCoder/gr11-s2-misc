# Sougato Chakrobortty
# 11/06/2026 Exam Preparation 2

# level 2

import random

times = 0

for i in range(1000):
    if random.randint(1, 6) + random.randint(1, 6) == 7:
        times += 1

print(f"Level 2: A 7 was rolled {times} times.")

# level 3

zeros = []

for i in range(12):
    zeros.append(0)

print(f"Level 3: {zeros}")

# level 4 (requires level 3)

zeros.pop(-1)

for i in range(1000):
    roll = random.randint(1, 6) + random.randint(1, 6)

    zeros[roll - 2] += 1

for i in range(len(zeros)):
    print(f"Level 4, {i + 2}: {zeros[i]} times")

    print(f"Level 4, {i + 2}:", "*" * zeros[i] // 1000 * 100)
