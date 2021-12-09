# program menyimpan data peminjaman buku

dataFile = open('PinjamBuku.txt', 'a')

from datetime import *

#membaca tangal sekarang
skrg = datetime.date(datetime.now())

#tanggal maksimal pengembalian
kembali = skrg + timedelta(days=7)

tglskrg = str(skrg)
tglkembali = str(kembali)

while True:
    kode = input('Masukkan Kode Member: ')
    nama = input('Masukkan Nama Member: ')
    judul = input('Masukkan Judul Buku: ')
    
    myString = kode+'|'+nama+'|'+judul+'|'+tglskrg+'|'+tglkembali+'\n'
    dataFile.write(myString)
    ans = input('Ulangi lagi (y/n): ')
    if ans in ('N', 'n'):
        break
    
dataFile.close()
