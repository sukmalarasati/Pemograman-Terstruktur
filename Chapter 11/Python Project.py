from datetime import *
def diffDate():
    skrg = datetime.date(datetime.now())
    x = date(2021, 12, 1)
    delta = skrg - x
    return delta.days

print('Selisihnya adalah: ', diffDate(), 'hari')
