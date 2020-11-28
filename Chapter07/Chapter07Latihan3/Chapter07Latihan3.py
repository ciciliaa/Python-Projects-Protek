print("----------------------------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("----------------------------------------------")

file = open("d:/data.txt", "a")
try:
    bilangan = print(input("Masukkan bilangan bulat: "))
    print("Lagi (y/n): ")
    pilihan = input("Mau lagi (y/n): ")
    if(pilihan == "y"):
        print(input("Data yang mau ditambahkan: "))
        print(input("Mau lagi (y/n): "))
        if(pilihan == "y"):
            print(input("Data yang mau ditambahkan: "))
            print(input("Mau lagi (y/n): "))
    else:
        print("Bilangan tidak valid")
except TypeError:
    print("Bukan bilangan bulat")
