banyak = int(input('Berapa banyak nama yang ingin Anda masukan? '))
name = []

for i in range(banyak):
    nama = str(input('Masukkan Nama Ke-' + str(i+1) + ': '))
    name.append(nama)

name.sort()

for nama in name:
    print(nama, '(', len(nama), 'karakter )')
