file = open("chapter10praktikum2.txt", "a")

i = 1
while(i == 1):
    nim = print(input("Masukkan NIM       : "))
    nama = print(input("Masukkan Nama Mhs : "))
    alamat = print(input("Masukkan Alamat   : "))

    pilihan = print(input("Ulangi input lagi (y/n) : "))
    if (pilihan == "y"):
        i = 1
    elif (pilihan == "n"):
        i = false

        file.write(nim + "|" + nama + "|" + alamat)

file.close()

