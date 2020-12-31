cari = print(input("Masukkan NIM yang dicari : "))

file = open("chapter10praktikum2", "r")
buka = file.readlines()

for i in range(len(buka)):
    if(cari in buka[i]):
        x = buka[i].split("|")
        print("Data Mahasiswa")
        print("NIM     : ", x[0])
        print("Nama    : ", x[1])
        print("Alamat  : ", x[2])
    else:
        print("Data mahasiswa tidak ditemukan")
        
