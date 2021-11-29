import random
string = input('Masukkan kata yang ingin diacak: ')
loop = int(input('Berapa kali pengacakan? '))
def shuffleString (x, n):
    listKata = []
    while True:
        kata = ''.join(random.sample(x, len (x)))
        if kata in listKata:
            continue
        else:
            listKata.append(kata)
            n -= 1
            if n == 0:
                print(listKata)
                break

print('randomString(', string, loop,') -> ', end='')
shuffleString(string, loop)
