s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())

items = [s1, s2, s3, s4, s5]

items.sort()

items.pop(0)
items.pop(3)

d = int(input())

t = (items[0] + items[1] + items[2]) * d
print(t)
