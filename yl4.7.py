arv = 0
posArve = 0
negArve = 0
posSumma = 0
negSumma = 0
arve = int(input("Mitu arvu?"))
for i in range(arve):
    arv = int(input("Anna arv: "))
    if arv > 0:
        posArve += 1
        posSumma += arv
    elif arv < 0:
        negArve += 1
        negSumma += arv
    elif arv == 0:
        print("Ma ei arvesta nulli, sest see pole ei paaritu ega paarisarv.")
if posArve != 0:
    print("Positiivsete keskmine =",posSumma / posArve)
if negArve != 0:
    print("Negatiivsete keskmine =",negSumma / negArve)