ubahHuruf = ('MATEMATIKA', 'T', 'S')
string = ubahHuruf
mylist = list(ubahHuruf)
print(mylist)

def ubahHuruf(string):
    ubah = string.replace('T', 'S')
    print(ubah)
    return ubah

string = "MATEMATIKA"
ubahHuruf(string)
