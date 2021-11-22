buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}

namabuah = input("Masukkan buah yang ingin dibeli : ")
pembelian = int(input("berapa kg :"))

harga = int(buah[namabuah]) * pembelian
if namabuah in buah:
    print("Nama buah yang dibeli :", namabuah)
    print("Berapa Kg             :", pembelian)
    print("____________")
    print("total harga           :", harga)
