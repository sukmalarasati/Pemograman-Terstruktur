def penjumlahan(*myData):
    #init values
    sum=0
    for i in myData:
        sum += i

    hasil=sum
    print('Jumlahnya adalah:', hasil)


def rerata(*myData):
    #init values
    sum=0
    i=0

    #input myData
    for data in myData:
        sum += data
        i += 1

    hasil=sum/i
    print('Rata-ratanya adalah: ',hasil)

def maks(*myData):
    hasil = 0
    for i in myData:
        if i >= hasil:
            hasil= i
    print('Nilai Maksimumnya adalah: ',hasil)
    
def minimum(*myData):
    hasil = 99999999999
    for i in myData:
        if i<= hasil:
            hasil= i
    print('Nilai minimumnya adalah: ',hasil)
