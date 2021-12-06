myFile = open('sukaPython.txt', 'a')
teksAsli = 'SAYA SUKA PYTHON'
print(teksAsli)
i = 0
geser = int(input('Masukkan berapa banyak pergeseran: '))
for i in range(len(teksAsli)):
    t = teksAsli[i]
    x = ord(t)
    if x==32:
        print(chr(x), end='')
    elif x+geser>90:
        print(chr(65+((x+geser)-91)), end='')
    elif x!=32:
        x+=int(geser)
        y = chr(x)
        print(y, end='')
    i+=1
    myFile.write(y)

myFile.close()
