from random import randint
jumlah = 0
while True:
    bil = randint(0, 10)
    print(bil)
    jumlah = jumlah + 1
    if bil == 9:
        break
print('Jumlah perulangan = ' + str(jumlah))

