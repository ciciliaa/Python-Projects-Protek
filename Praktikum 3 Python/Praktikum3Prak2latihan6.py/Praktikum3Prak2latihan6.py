score = 100
print(" Hai..nama saya Mr.Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!")

bil = int(input('tebakan anda : '))
if (bil < 5):
    print("Hehehe... Bilangan tebakan anda terlalu kecil")
    score = score - 2
bil = int(input('tebakan anda : '))
if (bil > 5):
    print("Hehehe... Bilangan tebakan anda terlalu besar")
    score = score - 2
bil = int(input('tebakan anda : '))
if (bil == 5):
    print("Yeeee... Bilangan tebakan anda BENAR :-)")

print("Score anda = " + str(score)) 
