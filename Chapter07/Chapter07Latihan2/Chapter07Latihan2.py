try:
    print(input("Data yang mau ditambahkan: "))
    pilihan = input("Mau lagi (y/n): ")
    if(pilihan == "y"):
        print(input("Data yang mau ditambahkan: "))
        print(input("Mau lagi (y/n): "))
        if(pilihan == "y"):
            print(input("Data yang mau ditambahkan: "))
            print(input("Mau lagi (y/n): "))
    else:
        print("selesai")
except FileNotFoundError:
    print("File Tidak Ditemukan")
