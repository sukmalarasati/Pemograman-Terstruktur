def kuadrat(bil):
    kuadrat = []
    for i in bil:
        kuadrat.append(i ** 2)
    return kuadrat
bil = [2, 4, 6, 8]
print('bil = ', bil)
print('hasil kuadrat = ', kuadrat(bil))
