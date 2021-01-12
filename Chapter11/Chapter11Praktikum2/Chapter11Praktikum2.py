from datetime import*

buka = open("nomer2.txt", "a")

i = 1
while(i == 1):
    kode = input("Masukkan Kode Member :")
    nama = input("Masukkan Nama Member :")
    buku = input("Masukkan Judul Buku  :")

    pilihan = input("Ulangi lagi(y/n) :")
    if (pilihan == "y"):
        i = 1
    elif (pilihan == "n"):
        i = False
        
sekarang = datetime.date(datetime.now())
kembali = sekarang + timedelta(days=7)

pinjam = kode + "|" + nama + "|" + buku + "|" + str(sekarang) + "|" + str(kembali)

file.close()
