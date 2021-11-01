from operation import *

a = 10
b = 7
print(a,'+', b, '=', jumlah(a, b))
print(a,'-', b, '=', kurang(a, b))
print(a,'*', b, '=', kali(a, b))
print(a,'/', b, '=', bagi(a, b))

a = 2
b = 4
c = 6

print('a.', a, '+', b, '*', c, '-', b, '=', kurang(jumlah(a, kali(b, c)), b))

a = 4
b = 7
c = 6
d = 9

print('b.', '(', a, '+', b, ')', '*', '(', c, '-', d, ')', '=', kali(jumlah(a, b), kurang(c, d)))

a = 10
b = 2
c = 7
d = 5
e = 12
f = 34

print('c', '(', a, '+', b, ')', '/', '(', c, '+', d, ')', '/', '(', e, '-', f, ')', '=', bagi(bagi(jumlah(a, b), jumlah(c, d)), kurang(e, f)))
