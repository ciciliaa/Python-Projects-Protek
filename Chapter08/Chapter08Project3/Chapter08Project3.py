namaMhs = []

nama = print(input("Masukkan nama: "))
namaMhs.append(nama)
pilihan = input("Mau lagi? (y/n)")
if (pilihan == "y"):
    nama = print(input("Masukkan nama: "))
    pilihan = input("Mau lagi? (y/n)")
else:
    print("selesai")
namaMhs.sort()
for i in range(len(namaMhs)):
    print(namaMhs[i], ", len(namaMhs[r]), ")
