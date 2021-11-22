def sortStringByChar(myData):
    myData.sort(reverse = True, key = len)
    return(myData)

def getListNamaBuah():
    loop = 0
    data = []
    while loop < 4:
        namaBuah = (input('Masukkan Nama Buah: '))
        data.append(namaBuah)
        loop += 1
    return data

dataList = getListNamaBuah()

if(dataList):
    print('Hasil dari List: ', dataList)
    result = sortStringByChar(dataList)
    print('Hasil yang sudah urut: ', result)
