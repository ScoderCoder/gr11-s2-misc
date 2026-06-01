#!/usr/bin/python

ngoc = input()
minh = input()

ngoclist = []
minhlist = []

for i in ngoc:
    ngoclist.append(i)

for i in minh:
    minhlist.append(i)

if len(ngoclist) > len(minhlist):
    times = len(minhlist)
elif len(ngoclist) < len(minhlist):
    times = len(ngoclist)
else:
    times = len(ngoclist)

lend = len(ngoclist) - 1
lend2 = len(minhlist) - 1

for i in range(0, lend + 1):
    if ngoclist[i] == "R":
        ngoclist[i] = 3
    elif ngoclist[i] == "G":
        ngoclist[i] = 2
    elif ngoclist[i] == "B":
        ngoclist[i] = 1

for i in range(0, lend2 + 1):
    if minhlist[i] == "R":
        minhlist[i] = 3
    elif minhlist[i] == "G":
        minhlist[i] = 2
    elif minhlist[i] == "B":
        minhlist[i] = 1

ngoceats = 0
minheats = 0

#if times != 3:
#    times -= 1

while len(ngoclist) > 0 and len(minhlist) > 0:
#for i in range(1, times + 1):
    if ngoclist[0] == minhlist[0]:
        ngoceats +=1
        ngoclist.pop(0)
        minheats +=1
        minhlist.pop(0)
    elif ngoclist[0] > minhlist[0]:
        if (minhlist[0] == 1) and (ngoclist[0] == 3):
            minheats += 1
            ngoclist.pop(0)
        else:
            ngoceats +=1
            minhlist.pop(0)
    elif minhlist[0] > ngoclist[0]:
        if (ngoclist[0] == 1) and (minhlist[0] == 3):
            ngoceats +=1
            minhlist.pop(0)
        else:
            minheats +=1
            ngoclist.pop(0)

if len(ngoclist) > len(minhlist):
    ngoceats += len(ngoclist)
elif len(ngoclist) < len(minhlist):
    minheats += len(minhlist)

print(ngoceats)
print(minheats)

