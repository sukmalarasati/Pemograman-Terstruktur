print("Menu: ")
print("A. Tambah data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan Data Sayur")

dataSayur = ['bayam', 'kangkung', 'wortel', 'selada']
pilih = str(input("Masukkkan pilihan anda: "))

if pilih == "A":
    print("Pilihan anda adalah Tambah data sayur")
    dataSayur.append(input("Silahkan masukkan nama sayur yang ingin ditambahkan: "))
    print("Data sayur: ", dataSayur)

elif pilih == "B":
    try:
        print("Pilihan anda adalah Hapus data sayur")
        dataSayur.remove(input("Silahkan masukkan nama sayur yang ingin dihapus: "))
        print("Data sayur: ", dataSayur)
    except ValueError:
        print("Data tidak ditemukan")

elif pilih == "C":
    print("Pilihan anda adalah Tampilkan Data Sayur")
    print("Data sayur: ", dataSayur)
