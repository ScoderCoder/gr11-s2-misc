m = int(input())
mlist = []

for i in range(1, m + 1):
    mlist.append(input())

okok = len(mlist) - 1
y = 0
x = 0

ychanges = []
xchanges = []

times = 0

for i in range(0, okok + 1):
    if mlist[i][0] == "S":
        new = 0 - int(mlist[i][1])

     
        ychanges.append(new)
    elif mlist[i][0] == "N":
        new = int(mlist[i][1])

        ychanges.append(new)
    elif mlist[i][0] == "E":
        new = int(mlist[i][1])

        xchanges.append(new)
    elif mlist[i][0] == "W":
        new = int(mlist[i][1])

        xchanges.append(new)

print(xchanges)
print(ychanges)
print(max(ychanges))
print(min(ychanges))

for i in range(0, okok + 1):
    if mlist[i][0] == "S":
        new = 0 - int(mlist[i][1])

        if new >= min(ychanges) and new <= max(ychanges):
            times = 1
    elif mlist[i][0] == "N":
        new = int(mlist[i][1])

        if new >= min(ychanges) and new <= max(ychanges):

            times = 1
    elif mlist[i][0] == "E":
        x += int(mlist[i][1])
    elif mlist[i][0] == "W":
        x += int(mlist[i][1])


print(times)
