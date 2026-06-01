list1 = [1, 3, 5, 7, 2]
list2 = [2, 4, 6, 8, 9]
list3 = list1 + list2
list4 = []

if list1[0] < list2[0]:
    list4.append(list1[0])
    list3.remove(list1[0])
elif list1[0] > list2[0]:
    list4.append(list2[0])
    list3.remove(list2[0])
else:
    list4.append(list1[0])
    list4.append(list2[0])
    list3.remove(list1[0])
    list3.remove(list2[0])

for i in list3[:]:
    if i not in list3:
        continue

    nlist = list3[:]
    nlist.remove(i)

    for j in nlist:
        if j < i:
            list4.append(j)
            list3.remove(j)

    list4.append(i)
    list3.remove(i)

for i in list4:
    print(i, end = " ")
