list = [18, 22, 20, 19, 18, 17, 20, 21]
print("Vanuseid oli loendis kokku",len(list))
print("Vanim vanus loendis:",max(list))
print("Noorim vanus loendis:",min(list))
kokku = 0
arve = 0
kesk = 0
for el in list:
    kokku += el
for i in list:
    arve += 1
kesk = round(kokku/arve)
print("Vanuste kogusumma on: ",kokku)
print("Keskmine vanus on:",kesk)