buah = {'apel'     : 5000,
        'jeruk'    : 8500,
        'mangga'   : 7800,
        'duku'     : 6500}

def ratarataHargaBuah(buah):
    totalHarga = 0
    jumlah = 0

    for r,y in buah.items():
        totalHarga += y
        jumlah += 1

    ratarata = totalHarga/jumlah
    return ratarata

a = ratarataHargaBuah(buah)
print('Rata-rata harga buah adalah: ', a)
