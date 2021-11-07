print('-----------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('-----------------------------')

while True:
    try:
        bil = input('Masukkan bilangan bulat: ')
        bilbulat = [int(x) for x in bil]
        jumlah = 0
        for bil in bilbulat:
            jumlah += bil
        ratarata = jumlah/len(bilbulat)
        ulang = str(input('Lagi (y/n)? : '))
        if ulang == 'y':
            print(end='')
        elif ulang == 'n':
            print('Rata-ratanya adalah: ', ratarata)
            break
        else:
            print('Invalid input')
            break
    except ValueError:
        print('Bukan bilangan bulat')
