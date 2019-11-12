## segitiga('purwadhika')

kata = 'Purwadhika'
listkata = list(kata)
panjang1 = len(kata)
# print(kata[0])
# print(panjang1)
n = 5
o = 0

def soal1(x):
    num= 0 
    for row in range(0,5,1):
        for col in range(1, row+1):
            print(x[num], end=' ')
            num = num+1
        print()
    # n= 5
    # o = 0
soal1(kata)

def soal11(y):
    num= 0 
    for row in range(4,0,-1):
        for col in range(o+1, row+1):
            print(y[num], end=' ')
            num = num+1
        print()
soal11(kata)





##segitiga('Purwadhika Startup and Coding School @BSD')
kata2 = 'Purwadhika Startup and Coding School @BSD'
kata2edit = kata2.replace(' ', '')
def soal2(a): 
    n = 9
    o = 0
    num= 0 
    for row in range(o+1,n,1):
        for col in range(o+1, row+1):
            print(a[num], end=' ')
            num = num+1
        print()
soal2(kata2edit)

def soal22(b):
    n = 9
    o = 0
    num= 0 
    for row in range(n-1,o,-1):
        for col in range(o+1, row+1):
            print(b[num], end=' ')
            num = num+1
        print()
soal22(kata2edit)


# #segitigakata('kode')
kata3 = 'kode'
n = 9
o = 0
num= 0 
panjangkata3 = len(kata3)

def soal3(f):
    n = 9
    o = 0
    num= 0 
    if 0 <= panjangkata3 <= num:
        for row in range(o+1,n,1):
            for col in range(o+1, row+1):
                print(f[num], end=' ')
                num = num+1
            print()
        n = 9
        o = 0
        num= 0 
        for row in range(n-1,o,-1):
            for col in range(o+1, row+1):
                print(f[num], end=' ')
                num = num+1
            print()
    else:
        print('mohon  maaf, jumlah karakter tidak memenuhi syarat membentuk pola')
soal3(kata3)




# segitiga('kode python')

kata4= 'kode python'
kata4edit = kata4.replace(' ', '')
listkata = list(kata)
panjang1 = len(kata)

n = 5
o = 0

def soal4(h):
    num= 0 
    for row in range(0,5,1):
        for col in range(1, row+1):
            print(h[num], end=' ')
            num = num+1
        print()

soal4(kata4edit)

def soal44(i):
    num= 0 
    for row in range(4,0,-1):
        for col in range(o+1, row+1):
            print(i[num], end=' ')
            num = num+1
        print()
soal44(kata4edit)


# #segitigakata('Lintang')
kata5 = 'lintang'


def soal5(j):
    n = 9
    o = 0
    num= 0 
    if 0 <= panjangkata3 <= num:
        for row in range(o+1,n,1):
            for col in range(o+1, row+1):
                print(j[num], end=' ')
                num = num+1
            print()
        n = 9
        o = 0
        num= 0 
        for row in range(n-1,o,-1):
            for col in range(o+1, row+1):
                print(j[num], end=' ')
                num = num+1
            print()
    else:
        print('mohon  maaf, jumlah karakter tidak memenuhi syarat membentuk pola')
soal5(kata5)