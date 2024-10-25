##Begin1, Begin2
a = int(input('tomonni kiriting '))
P = 4*a
S=a**2
print('P = ', P)
print('S = ', S)


##Begin3

a = int(input('tomonni kiriting '))
b = int(input('tomonni kiriting '))
P = 2*(a+b)
S = a*b
print('P = ', P)
print('S = ', S)

#Begin4

pi = 3.14
d = float(input('diametrini kiriting '))
L = pi * d
print('L = ', L)

##Begin5

a = int(input('tomonni kiriting '))
V = a**3
S = 6*a**2
print('V = ', V)
print('S = ', S)

##Begin6

a = int(input('tomonni kiriting '))
b = int(input('tomonni kiriting '))
c = int(input('tomonni kiriting '))
V = a*b*c
S = 2*(a*b + b*c + a*c)
print('V = ', V)
print('S = ', S)

##Begin7

pi = 3.14
R = int(input('tomonni kiriting '))
L = 2*pi*R
S = pi*R**2
print('L = ', L)
print('S = ', S)

##Begin8

a = int(input('sonni kiriting '))
b = int(input('sonni kiriting '))
O = (a+b)/2
print('Orta arifmetigi = ', O)

##Begin9

a = int(input('a = '))
b = int(input('b = '))
G = abs((a*b)**0.5)
print('G = ', G)

##Begin10

sum = a + b
square_a = a**2
square_b = b**2
product = a * b
print('sum = ', sum)
print('square_a = ', square_a)
print('square_b = ', square_b)
print('product = ', product)

##Begin11

a = int(input("a: "))
b = int(input("b: "))
sum = a + b
product = a * b
mod_a = abs(a)
mod_b = abs(b)
print("Yig'indi: ", sum)
print("Ko'paytma: ", product)
print("|a|: ", mod_a, "|b|: ", mod_b)

##Begin12

a = int(input("a: "))
b = int(input("b: "))
c = (a**2 + b**2) ** 0.5
P = a + b + c
print("Gipotenuza: ", c)
print("Uchburchak perimetri: ", P)

##Begin13

R1 = int(input("R1: "))
R2 = int(input("R2: "))
pi = 3.14
S1 = pi * R1 ** 2
S2 = pi * R2 ** 2
S3 = S1 - S2
print("Aylanalarning yuzalar ayirmasi: ", S3)

##Begin14

L = float(input("L: "))
pi = 3.14
R = L / (2 * pi)
print("Aylaning radiusi: ", R)

##Begin15

S = float(input("S: "))
pi = 3.14
R = (S / pi) ** 0.5
D = 2 * R
print("Aylaning radiusi: ", R)
print("Aylaning diametri: ", D)

##Begin16

x1 = int(input("Birinchi nuqta koordinatasini kiriting: "))
x2 = int(input("Ikkinchi nuqta koordinatasini kiriting: "))
distance = abs(x2 - x1)
print("Nuqtalar orasidagi masofa: ", distance)

##Begin17

A = int(input("A nuqta koordinatasi: "))
B = int(input("B nuqta koordinatasi: "))
C = int(input("C nuqta koordinatasi: "))
AC = abs(C - A)
BC = abs(C - B)
total_length = AC + BC
print("AC va BC kesmalarining yig'indisi: ", total_length )

##Begin18

AC = abs(C - A)
BC = abs(C - B)
product = AC * BC
print("AC va BC kesmalarining ko'paytmasi: ", product )

##Begin19

x1 = int(input("x1 koordinatasi: "))
y1 = int(input("y1 koordinatasi: "))
x2 = int(input("x2 koordinatasi: "))
y2 = int(input("y2 koordinatasi: "))
perimeter = 2 * (abs(x2 - x1) + abs(y2 - y1))
area = abs(x2 - x1) * abs(y2 - y1)
print("To'rtburchakning perimetri: ", perimeter )
print("To'rtburchakning yuzi: ", area)

##Begin20

x1 = int(input("Birinchi nuqta x1 koordinatasi: "))
y1 = int(input("Birinchi nuqta y1 koordinatasi: "))
x2 = int(input("Ikkinchi nuqta x2 koordinatasi: "))
y2 = int(input("Ikkinchi nuqta y2 koordinatasi: "))
distance = ((x2 - x1)2 + (y2 - y1)2) ** 0.5
print("Nuqtalar orasidagi masofa: ", distance)

##Begin21

x1, y1 = int(input("x1: ")), int(input("y1: "))
x2, y2 = int(input("x2: ")), int(input("y2: "))
x3, y3 = int(input("x3: ")), int(input("y3: "))
a = ((x2 - x1)2 + (y2 - y1)2) ** 0.5
b = ((x3 - x2)2 + (y3 - y2)2) ** 0.5
c = ((x1 - x3)2 + (y1 - y3)2) ** 0.5
p = (a + b + c) / 2
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print("Uchburchak perimetri: ", a + b + c)
print("Uchburchak yuzi: ", area )

##Begin22

A = int(input("A ning qiymati: "))
B = int(input("B ning qiymati: "))
A, B = B, A
print("A = ", A , "B = " B )

##Begin23

A = int(input("A ning qiymati: "))
B = int(input("B ning qiymati: "))
C = int(input("C ning qiymati: "))
A, B, C = B, C, A
print("A = ", A, "B = ", B, "C = ", C)

##Begin24

A = int(input("A ning qiymati: "))
B = int(input("B ning qiymati: "))
C = int(input("C ning qiymati: "))
A, B, C = C, A, B
print("A = ", A, "B = ", B, "C = ", C)

##Begin25

x = int(input("x ning qiymatini kiriting: "))
y = 3 * x6 - 6 * x2 - 7
print("Funktsiya qiymati: y = ", y)

##Begin26

x = int(input("x ning qiymatini kiriting: "))
y = 4 * (x - 3)6 - 7 * (x - 3)3 + 2
print("Funktsiya qiymati: y = ", y)

##Begin27

A = int(input("A sonini kiriting: "))
A2 = A ** 2
A3 = A ** 3
A5 = A ** 5
A10 = A ** 10
A15 = A ** 15
print("A^2 = ", A2, "A^3 = ", A3, "A^5 = ", A5, "A^10 = ", A10, "A^15 = ", A15)

##Begin28

alpha = int(input("Burchak: "))
radians = alpha * 3.14 / 180
print("Burchak radianlarda: ", radians)

##Begin29

radians = float(input("Burchak: "))
degrees = radians * 180 / 3.14
print("Burchak graduslarda: ", degrees)

##Begin30 

radians = float(input("Burchak: "))
pi = 3.14
degrees = radians * (180 / pi)
print("Burchak graduslarda: ", degrees)

##Begin31

TF = int(input("haroratni kiriting: "))
TC = (TF - 32) * 5 / 9
print('TC = ' ,TC,"°C")

##Begin32

TC = int(input("haroratni kiriting: "))
TF = (TC * 9 / 5) + 32
print('TC = ',TF,"°F")

##Begin33

X = int(input("1 kg konfetning narxini kiriting: "))
Y = int(input("Y kg konfetning og'irligini kiriting: "))
Total = X * Y
print('Total = ', Total)

##Begin34

A = int(input("1 kg shokolad narxini kiriting: "))
B = int(input("1 kg konfet narxini kiriting: "))
X = int(input("X kg shokoladni kiriting: "))
Y = int(input("Y kg konfetni kiriting: "))
choco_total = A * X
candy_total = B * Y
print('Shokolad va konfet farqi: ', choco_total - candy_total)

##Begin35

V = int(input("Qayiqning tezligini kiriting: "))
U = int(input("Daryoning oqim tezligini kiriting: "))
S = int(input("Qayiq yurgan masofani kiriting: "))
T1_oqim_boyicha= S / (V + U) 
T2_oqimga_qarshi= S / (V - U) 
print("Oqim bo'yicha harakatlanish vaqti: ", T1_oqim_boyicha, "soat")
print(f"Oqimga qarshi harakatlanish vaqti: ", T2_oqimga_qarshi, "soat")

##Begin36

V1 = int(input("Birinchi avtomobilning tezligini kiriting: "))
V2 = int(input("Ikkinchi avtomobilning tezligini kiriting: "))
T = int(input("Orasidagi vaqtni kiriting: "))
S = (V1 + V2) * T
print("Ular orasidagi masofa: ", S, "km")

##Begin37

V1 = int(input("Birinchi avtomobilning tezligini kiriting: "))
V2 = int(input("Ikkinchi avtomobilning tezligini kiriting: "))
T = int(input("Orasidagi vaqtni kiriting: "))
if V1 > V2:
    S = (V1 - V2) * T
else:
    S = (V2 - V1) * T
print("Ular orasidagi masofa: ", S, "km")

##Begin38

A = int(input("A koeffitsientni kiriting: "))
B = int(input("B koeffitsientni kiriting: "))
if A != 0:
    x = -B / A
    print("Tenglama yechimi: x = ", x)
else:
    print("A nolga teng bo'lishi mumkin emas.")

##Begin39

A = int(input("A koeffitsientni kiriting: "))
B = int(input("B koeffitsientni kiriting: "))
C = int(input("C koeffitsientni kiriting: "))
D = B**2 - 4 * A * C 
if D > 0:
    x1 = (-B + D**0.5) / (2 * A)
    x2 = (-B - D**0.5) / (2 * A)
    print("Tenglama ikki yechimga ega: x1 = ", x1, "x2 = ", x2)
elif D == 0:
    x = -B / (2 * A)
    print("Tenglama bitta yechimga ega: x = ", x)
else:
    print("Tenglama haqiqiy yechimga ega emas.")    

##Begin40

A1 = int(input("A1 koeffitsientni kiriting: "))
B1 = int(input("B1 koeffitsientni kiriting: "))
C1 = int(input("C1 ni kiriting: "))
A2 = int(input("A2 koeffitsientni kiriting: "))
B2 = int(input("B2 koeffitsientni kiriting: "))
C2 = int(input("C2 ni kiriting: "))
D = A1 * B2 - A2 * B1 
if D != 0:
    x = (C1 * B2 - C2 * B1) / D
    y = (A1 * C2 - A2 * C1) / D
    print("Sistema yechimlari: x = ", x, "y = ", y)
else:
    print("Sistema yechimga ega emas.")