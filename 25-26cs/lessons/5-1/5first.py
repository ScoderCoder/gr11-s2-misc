nums = []

def asknum():
    numb = int(input("Enter a number: "))
    return numb

for i in range(1, 11):
    nums.append(asknum())

nums.sort()

median = nums[(len(nums) / 2)]

print(nums)
