try:
    namaFile = input('Masukkan nama file: ')
    file = open('d:/myfile.txt', 'r')
    print('isi file d:/myfile.txt', 'adalah: ')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')
