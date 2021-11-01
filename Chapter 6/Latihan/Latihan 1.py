import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def isPythagoras(a, b, c):
    return c**2-b**2==a**2

if (isPythagoras(a, b, c)):
    print('True')
else:
    print('False')
