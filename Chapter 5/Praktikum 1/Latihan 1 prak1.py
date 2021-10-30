#status kelulusan ujian mahasiswa
#memasukkan nilai

BhsIndo = int(input('Masukkan nilai Bhs Indonesia :'))
IPA     = int(input('Masukkan nilai IPA :'))
MTK     = int(input('Masukkan nilai MTK :'))

if(BhsIndo >= 60) and (IPA >= 60) and (MTK > 70):
    print('LULUS')
else:
    print('TIDAK LULUS')
