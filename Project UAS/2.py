file = open("dataKaryawan.dat", "r")
file.readlines()

file = [{"kode" : "001", "nama" : "Natali", "alamat" : "Ponorogo", "gol" : "A", "gaji" : "4.000.000", "tgl" : "3 Desember 1997", "usia" : "23 th"},
        {"kode" : "002", "nama" : "Giovan", "alamat" : "Surakarta", "gol" : "A", "gaji" : "4.000.000", "tgl" : "4 Juni 2000", "usia" : "20 th"},
        {"kode" : "003", "nama" : "Kanaya", "alamat" : "Surabaya", "gol" : "C", "gaji" : "5.000.000", "tgl" : "5 Agustus 2000", "usia" : "20 th"}]

print("-------------------------------------------------------------")
print("KODE KARY".ljust(5, " "), "NAMA KARY".ljust(5, " "), "ALAMAT".ljust(5, " "), "GOL".ljust(5, " "), "GAJI POKOK".rjust(5, " "), "TGL LAHIR".ljust(5, " "), "USIA".rjust(5, " "))
print("-------------------------------------------------------------")

for data in file:
    print(data["kode"].ljust(5, " "),
          data["nama"].ljust(5, " "),
          data["alamat"].ljust(5, " "),
          data["gol"].ljust(5, " "),
          data["gaji"].rjust(5, " "),
          data["gaji"].ljust(5, " "),
          data["usia"].rjust(5, " "))

print("-------------------------------------------------------------") 


