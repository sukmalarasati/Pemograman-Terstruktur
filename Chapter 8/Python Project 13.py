def dataTertinggi(data):
    # mendapat nim, nama mhs yang nilai akhir tinggi
    # rumus nilai akhir = (nilai MID + 2 Nilai UAS)/3
    hasil = {}
    nilaiAkhir = None
    for x in data:
        nilai = (x['mid'] + 2 * x['uas'])/3
        if(nilaiAkhir is None) or (nilai>nilaiAkhir):
            nilaiAkhir = nilai
            hasil ['nim'] = x['nim']
            hasil ['nama'] = x['nama']
    return hasil


nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

hasil = dataTertinggi(nilaiMhs)
if(bool(hasil)):
    print('Mahasiswa yang memiliki nilai akhir tertinggi: {0}, nim {1}'.format(hasil['nama'], hasil['nim']))
