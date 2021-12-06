file = open('sukaPython.txt', 'r')
myFile = open('SandiCaesar7.txt', 'a')
read = file.read()
teksSandi = 'TBZB TVLB QZUIPO', 'UCAC UWMC RAVJQP', 'VDBD VXND SBWKRQ', 
print(teksSandi)
i = 0
sandi = int(input('Masukkan pergeseran sandi: '))
for i in range(len(teksSandi)):
    t = teksSandi[i]
    x = ord(t)
    if x==32:
        print(chr(x), end='')
    elif x+sandi>90:
        print(chr(65+((x+sandi)-91)), end='')
    elif x!=32:
        x+=int(sandi)
        y = chr(x)
        print(y, end='')
    myFile.write(y)

file.close()
myFile.close()
