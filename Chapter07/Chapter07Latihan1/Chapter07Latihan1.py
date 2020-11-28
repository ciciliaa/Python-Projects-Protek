try:
    nama = print(input("Masukkan nama file: "))
    print("Isi file adalah :")
except FileNotFoundError:
    print("File tidak ditemukan")
