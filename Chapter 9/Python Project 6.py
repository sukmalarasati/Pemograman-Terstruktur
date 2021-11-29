nilai = [{'nim' : 'A01', 'nama' : 'AGUSTINA', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'BUDI', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'CHICHA', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'DONNA', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'FATIMAH', 'mid' : 70, 'uas' : 100}]

for data in nilai:
    nilaiAkhir = (data['mid'] + (2 * data['uas'])) / 3  
    data['nilaiAkhir'] = round(nilaiAkhir, 1)
    if nilaiAkhir >= 60:
        data['status'] = 'LULUS'
    else:
        data['status'] = 'TIDAK LULUS'

print('===============================================================')
print('NIM     NAMA          N.MID        N.UAS    N.AKHIR     STATUS' )
print('---------------------------------------------------------------')

for i in range(len(nilai)):
    print(nilai[i]['nim'].ljust(8), end='')
    print(nilai[i]['nama'].ljust(14), end='')
    print(str(nilai[i]['mid']).rjust(5), end='')
    print(str(nilai[i]['uas']).rjust(13), end='')
    print(str(nilai[i]['nilaiAkhir']).rjust(11), end='')
    print(nilai[i]['status'].rjust(10))

print('---------------------------------------------------------------')
