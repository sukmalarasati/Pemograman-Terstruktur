a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

#2-4
a.insert(2, 10)
a.append(4)
a.sort()
print(a)

b.insert(1, 15)
b.append(8)
b.sort()
print(b)

#5
c = a[0:8]
d = b[2:10]
print('c = ', c)
print('d = ', d)

#6
hasil = []
cplusd = []
if len(c) == len(d):
    for i in range(len(c)):
        cplusd=c[i]+d[i]
        hasil.append(cplusd)
    print('e = ',hasil)
    
#7
list = hasil
myTuple = tuple(hasil)
print('e = ', myTuple)

#8
print('Nilai minimum elemen dari e adalah', min(myTuple))
print('Nilai maximum elemen dari e adalah', max(myTuple))
print('Nilai jumlah seluruh elemen dari e adalah', sum(myTuple))

#9
myString = ('python adalah bahasa pemograman yang menyenangkan')

#10
print('Huruf penyusun')
hurufpenyusun = set(myString)
print(hurufpenyusun)

#11
print('Huruf penyusun setelah diubah ke list')
Tuple = hurufpenyusun
myList = list(hurufpenyusun)
print (myList)
