# script struk rincian gaji karyawan

kode = int(input("Masukkan kode karyawan     : "))
nama = input("Masukkan nama karyawan     : ")
gol = input("Masukkan golongan          : ")
           
print("========================================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("--------------------------------------------------------")

print("Nama Karyawan     : " + nama + " (Kode : " + str(kode) +") ")
print("Golongan          : " + gol + " ")
print("--------------------------------------------------------")


if (gol == "A"):
    gaPok = 10000000
    ptg   = 2.5 / 100 * 10000000
    gaBer = gaPok - ptg
    print("Gaji Pokok       : Rp " + str(gaPok) + ") ")
    print("Potongan (2.5%)  : Rp " + str(ptg) + ") ")
    print("--------------------------------------------------------" " - ")
    print("Gaji Bersih      : Rp " + str(gaBer) + ") ")

if (gol == "B"):
    gaPok = 8500000
    ptg   = 2.0 / 100 * 10000000
    gaBer = gaPok - ptg
    print("Gaji Pokok       : Rp " + str(gaPok) + ") ")
    print("Potongan (2.0%)  : Rp " + str(ptg) + ") ")
    print("--------------------------------------------------------" " - ")
    print("Gaji Bersih      : Rp " + str(gaBer) + ") ")

if (gol == "C"):
    gaPok = 7000000
    ptg   = 1.5 / 100 * 10000000
    gaBer = gaPok - ptg
    print("Gaji Pokok       : Rp " + str(gaPok) + ") ")
    print("Potongan (1.5%)  : Rp " + str(ptg) + ") ")
    print("--------------------------------------------------------" " - ")
    print("Gaji Bersih      : Rp " + str(gaBer) + ") ")

if (gol == "D"):
    gaPok = 5500000
    ptg   = 1.0 / 100 * 10000000
    gaBer = gaPok - ptg
    print("Gaji Pokok       : Rp " + str(gaPok) + ") ")
    print("Potongan (1.0%)  : Rp " + str(ptg) + ") ")
    print("--------------------------------------------------------" " - ")
    print("Gaji Bersih      : Rp " + str(gaBer) + ") ")
