buah = {'apel' : 5000,
            'jeruk' : 8500,
            'mangga' : 7800,
            'duku' : 6500}

print("Daftar buah : apel,jeruk,mangga,duku")
print(input("Nama buah yang dibeli : "))
print(input("Berapa Kg             : "))
print("-----------------------------------")
print("Total harga           : ")

while pilih:
    pilih = input("Beli buah yang lain (y/n)? ")
    if(pilih == "y"):
        print(input("Nama buah yang dibeli : "))
        print(input("Berapa Kg             : "))
    else:
        break

        while menu:
            menu = ("A. Tambah data buah, B. Beli buah")
            if(menu == "A. Tambah data buah"):
                print(input("Masukkan nama buah    :")
                print(input("Masukkan harga satuan :")
            else:
                break
