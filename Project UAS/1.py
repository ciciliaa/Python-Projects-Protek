file = open("dataKaryawan.dat", "a")

x = True
while(x == True):
    nip = input("Masukkan NIP       :")
    nama = input("Masukkan Nama      :")
    alamat = input("Masukkan Alamat    :")
    golongan = input("Masukkan Golongan  :")
    tglLahir = input("Masukkan Tgl Lahir :")

    file.write(nip + '|' + nama + '|' + alamat + '|' + golongan + '|' + tglLahir + '/n')
    pilihan = input("Tambah data(y/n)     :")
    
    if(pilihan == "y"):
        x = True
    elif(pilihan == "n"):
        x = False
    else:
        print("selesai")
        continue

file.close()
