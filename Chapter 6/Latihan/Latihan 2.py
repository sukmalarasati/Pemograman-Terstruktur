#starFormation1
def starFormation1(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end='')
        print('')
starFormation1(4)
print('')


#starFormation2
def starFormation2(n):
    for i in range(n, 0,-1):
        for j in range(i):
            print('*', end='')
        print('')
starFormation2(4)
print('')


#starFormation3
def starFormation1(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end='')
        print('')
def starFormation2(n):
    for i in range(n, 0,-1):
        for j in range(i):
            print('*', end='')
        print('')
starFormation1(4)
starFormation2(3)
print()
