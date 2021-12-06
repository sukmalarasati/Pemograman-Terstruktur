# program mencari data mhs

dataFile = open('datamahasiswa.txt', 'r')
bacaFile = dataFile.read().splitlines()

nim = input('Masukkan NIM yang mau dicari: ')
print()

for i in range(len(bacaFile)):
    data = bacaFile[i].split('|')
    if nim == data[0]:
        status = 'ada'
        print('Data Mahasiswa')
        print('NIM    : ' + data[0])
        print('Nama   : ' + data[1])
        print('Alamat : ' + data[2])
        break
    else:
        status = 'tidak ada'

if status == 'tidak ada':
    print('Data mahasiswa tidak ditemukan')

dataFile.close()
