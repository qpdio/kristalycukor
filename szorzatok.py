#1.feladat szorzás
while True:
    y=int(input("Kérem az első számot: "))
    if y==-1:
        break
    x=int(input("Kérem a második számot: "))
    if x==-1:
        break
    z=1
    for i in range(y,x+1):
        z*=i
    print(f"Az intervallumban található számok szorzata: {z}")

#1.feladat összeadás
while True:
    y=int(input("Kérem az első számot: "))
    if y==-1:
        break
    x=int(input("Kérem a második számot: "))
    if x==-1:
        break
    z=0
    for i in range(y,x+1):
        z+=i
    print(f"Az intervallumban található számok összege: {z}")

#2.feladat

import math

def atfogo(a,b):
    c=math.sqrt(5*math.sqrt(a*b))
    if c<5:
        raise ValueError("Hiba! Túl kicsi a háromszög!")
    return c

print("2. feladat: Derékszögű háromszög átfogója")
print("Kérem a két befogó méretét!")
while True:
    a=float(input("Egyik befogó mérete: "))
    if a==-1:
        break
    b=float(input("Másik befogó mérete: "))
    if b==-1:
        break
    try:
        print(f"Az átfogó mérete: {atfogo(a,b):.2f}")
    except ValueError as hiba:
        print(hiba)



def terület(x,y):
    z=x*y
    if z<100:
        raise ValueError("Hiba! Túl kicsi a terület!")
    return z

while True:
    x=int(input("Kérem az első számot(m): "))
    if x==0:
        break
    y=int(input("Kérem a második számot(m): "))
    if y==0:
        break
    try:
        print(f"Telek területe: {terület(x,y)} m2")
    except ValueError as hiba:
        print(hiba)