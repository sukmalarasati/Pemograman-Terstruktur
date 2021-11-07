namaFile = input('Masukkan nama file: ')
try:
    while True:
        file = open('myfile', 'a')
        data = input('Data yang mau ditambahkan: ')
        file.write(data)
        file.close()
        ulang = input('Lagi (y/n)? : ')
        if ulang == 'n':
            break
except FileNotFoundError:
    print('File tidak ditemukan')
