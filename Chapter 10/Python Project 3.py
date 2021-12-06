# program baca data mhs

dataFile = open('datamahasiswa.txt', 'r')
dataList = []
data = dataFile.readlines()

for i in range(len(data)):
    fix = data[i].replace('\n', ' ')
    pecahData = fix.split('|')
    dataDict = {'nim': pecahData[0], 'nama': pecahData[1], 'alamat': pecahData[2]}
    dataList.append(dataDict)

print(dataList)
dataFile.close()
