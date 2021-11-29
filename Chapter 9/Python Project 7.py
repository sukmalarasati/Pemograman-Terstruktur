mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('===============================================================')
print('NIM        NAMA MAHASISWA      TGL LAHIR           TEMPAT LAHIR' )
print('---------------------------------------------------------------')

for data in mhs:
    splitData = data.split(':')
    space = 11
    for i in range(len(splitData)):
        if i == 2:
            tanggal = splitData[i].split('-')
            tanggal.reverse()
            print('/'.join(tanggal).ljust(space), end='')
            continue
        print(splitData[i].ljust(space), end='')
        space= 20
    print('')

print('---------------------------------------------------------------')
