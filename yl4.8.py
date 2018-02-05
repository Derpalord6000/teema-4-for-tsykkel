list1 = [1, 2, 3, 2, 5, 2, 2]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print("Vana list:",list1)
print("Kordusteta list:",list2)