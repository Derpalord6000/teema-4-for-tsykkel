list = []
paaris = []
y = True
while y == True:
    ans = input("Mis arvu soovid lisada? Katkestamiseks vajuta lihtsalt enter.")
    if ans == "":
        y = False
    else:
        y = True
        list.append(int(ans))

for i in list:
    if i % 2 == 0:
        paaris.append(1)

paar = len(paaris)

print("Arvudeelist oli",list)
print("Paarisarve oli listis",paar)