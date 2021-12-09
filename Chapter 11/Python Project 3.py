from datetime import *
from os import truncate

dataFile = open('PinjamBuku.txt', 'r')

bacaFile = dataFile.read().splitlines()

fileBaca = []

def diffDate():
    global x
    global skrg
    skrg = datetime.date(datetime.now())
    x = date(2021, 12, 15)
    delta = skrg - x
    return delta.days

denda = diffDate() * 2000
tglpinjam = date(2021, 12, 8)

for i in range(len(bacaFile)):
    fix = bacaFile[i].replace('\n', '') 
    split = fix.split('|')
    Dict = {'kode': split[0], 'nama': split[1], 'judul': split[2]}
    fileBaca.append(Dict)



while True:
    nim = input('Masukkan Kode Member: ')

    for i in range(len(fileBaca)):
        if nim in fileBaca[i]['kode']:
            print('Data Peminjaman Buku')
            print('Kode Member              : ', str(fileBaca[i]['kode']))
            print('Nama Member              : ', str(fileBaca[i]['nama']))
            print('Judul Buku               : ', str(fileBaca[i]['judul']))
            print('Tanggal Mulai Peminjaman : ', tglpinjam)
            print('Tanggal Maks Peminjaman  : ', x)
            print('Tanggal Pengembalian     : ', skrg)
            print('Terlambat                : ', diffDate())
            print('Denda                    : ', denda)
    break
else:
    status = 'tidak ada'

if nim not in fileBaca[0]['kode']:
    if nim not in fileBaca[1]['kode']:
        if nim not in fileBaca[2]['kode']:
            print('\'Data mahasiswa tidak ditemukan\'')

dataFile.close()
