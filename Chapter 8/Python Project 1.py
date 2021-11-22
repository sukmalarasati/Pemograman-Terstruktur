try:
    banyakbil = int(input('Berapa banyak bilangan yang ingin Anda masukan? '))
    bil = []

    for i in range(banyakbil):
        angka = int(input('Masukkan Angka Ke-' + str(i+1) + ': '))
        bil = bil + [angka]

    bil.sort(reverse=True)
    print('Angka yang Anda masukkan adalah ', bil)

except ValueError:
    print('Maaf, input yang Anda masukkan bukan termasuk angka')
