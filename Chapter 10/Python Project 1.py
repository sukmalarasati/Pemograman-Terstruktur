# open file dan baca file
def read():
    myFile = open('bilangan.txt', 'r')
    baca = myFile.readlines()

    baca1 = []
    
    for i in range(len(baca)):
        fix = baca[i].replace('\n', '')
        baca1 += [fix]

    global ganjil
    global genap
    ganjil = []
    genap = []
    
    for i in range(len(baca1)):
        if int(baca1[i])%2 == 0:
            genap += [baca1[i]]
        elif int(baca1[i])%2 == 1:
            ganjil += [baca1[i]]
        myFile.close()

read()
print('Banyaknya bilangan genap: ', len(genap))
print('Banyaknya bilangan ganjil: ', len(ganjil))
