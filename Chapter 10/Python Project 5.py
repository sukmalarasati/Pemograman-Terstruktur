myFile = open('bil12.txt', 'r')
HasilJumlah = open('HasilJumlah.txt', 'a')
read = myFile.readlines()

for i in range(len(read)):
    replace = read[i].replace("\n", "") 
    bil = replace.split("|")
    print(str(int(bil[0]) + int(bil[1])))
    HasilJumlah.write(str(int(bil[0]) + int(bil[1]))+"\n")

myFile.close()
HasilJumlah.close()
