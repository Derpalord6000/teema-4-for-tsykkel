"""

x = 7
kordaja = 1
c = 0
while  c < 100:
    c = x * kordaja
    kordaja += 1
    if 10 < c and c < 100:
        print(c)
    else:
        print("x")

"""

for i in range(10,100):
    if i % 7 == 0:
        print(i)