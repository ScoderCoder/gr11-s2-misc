num = int(input("Please enter your number: "))
times = 0
originum = num

while num % 2 == 0 and num != 0:
    num = num / 2
    times += 1

print(f"{originum} is divisible {times} times.")
