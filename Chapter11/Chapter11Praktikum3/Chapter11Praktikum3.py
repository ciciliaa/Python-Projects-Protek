from datetime import *

file = open("nomer2.txt", "r")
data = file.readlines()

member = input("Masukkan Kode Member :")


i = 0
for i in range(len(data)):
    splitData = data[i].split("|")

    if kode in splitData:
        sekarang = datetime.date(datetime.now())
        terlambat = getTerlambat(sekarang)
        if(terlambat <= 0):
            print("Tidak Terlambat, Tidak Ada Denda")
        elif(terlambat > 0):
            print("terlambat:", "Rp" + str(terlambat*2000))
            print("Data Pinjaman Buku")
            print("Kode Member              :")
            print("Nama Member              :")
            print("Judul Buku               :")
            print("Tanggal Mulai Peminjaman :")
            print("Tanggal Maks Peminjaman  :")
            print("Tanggal Pengembalian     :")
            print("Terlambat                :")
            print("Denda                    :")
        else:
            print("Data Tidak Ditemukan")

file.close()
