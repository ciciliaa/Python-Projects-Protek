# script struk rincian gaji karyawan

kode = int(input("Masukkan kode karyawan     : "))
nama = input("Masukkan nama karyawan     : ")
gol = input("Masukkan golongan          : ")
status = int(input("Masukkan status (1:menikah, 2:belum) : "))
if (status == '1'):
    anak = int(input("Masukkan jumlah anak          : "))
    statusMenikah = ("Sudah Menikah")
else:
    anak = 0
    statusMenikah = ("Belum Menikah")

    
print("========================================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("--------------------------------------------------------")

print("Nama Karyawan             : " + nama + " (Kode : " + str(kode) + ") ")
print("Golongan                  : " + gol + " ")
print("Status Menikah            : " + statusMenikah + " ")
print("Jumlah  Anak              : " + str(anak) + " ")
print("--------------------------------------------------------")

if (gol == "A"):
    gaPok = 10000000
    tjgIsSu = 10 / 100 * 10000000
    tjgAn = 5 / 100 * 10000000
    gaKot = gaPok + tjgIsSu + tjgAn
    ptg   = 2.5 / 100 * gaKot
    gaBer = gaKot - ptg
    print("Gaji Pokok               : Rp " + str(gaPok) + " ")
    print("Tunjangan Istri/Suami    : Rp " + str(tjgIsSu) + " ")
    print("Tunjangan Anak           : Rp " + str(tjgAn) + " ")
    print("--------------------------------------------------------" " + ")
    print("Gaji Kotor               : Rp " + str(gaKot) + " ")
    print("Potongan (2.5%)          : Rp " + str(ptg) + " ")
    print("--------------------------------------------------------" " - ")
    print("Gaji Bersih              : Rp " + str(gaBer) + " ")

if (gol == "B"):
    gaPok = 8500000
    tjgIsSu = 10 / 100 * 8500000
    tjgAn = 5 / 100 * 8500000
    gaKot = gaPok + tjgIsSu + tjgAn
    ptg   = 2.0 / 100 * gaKot
    gaBer = gaKot - ptg
    print("Gaji Pokok               : Rp " + str(gaPok) + " ")
    print("Tunjangan Istri/Suami    : Rp " + str(tjgIsSu) + ") ")
    print("Tunjangan Anak           : Rp " + str(tjgAn) + " ")
    print("--------------------------------------------------------" " + ")
    print("Gaji Kotor               : Rp " + str(gaKot) + " ")
    print("Potongan (2.0%)          : Rp " + str(ptg) + " ")
    print("--------------------------------------------------------" " - ")
    print("Gaji Bersih              : Rp " + str(gaBer) + " ")

if (gol == "C"):
    gaPok = 7000000
    tjgIsSu = 10 / 100 * 7000000
    tjgAn = 5 / 100 * 7000000
    gaKot = gaPok + tjgIsSu + tjgAn
    ptg   = 1.5 / 100 * gaKot
    gaBer = gaKot - ptg
    print("Gaji Pokok               : Rp " + str(gaPok) + " ")
    print("Tunjangan Istri/Suami    : Rp " + str(tjgIsSu) + " ")
    print("Tunjangan Anak           : Rp " + str(tjgAn) + " ")
    print("--------------------------------------------------------" " + ")
    print("Gaji Kotor               : Rp " + str(gaKot) + " ")
    print("Potongan (1.5%)          : Rp " + str(ptg) + " ")
    print("--------------------------------------------------------" " - ")
    print("Gaji Bersih              : Rp " + str(gaBer) + " ")

if (gol == "D"):
    gaPok = 5500000
    tjgIsSu = 10 / 100 * 5500000
    tjgAn = 5 / 100 * 5500000
    gaKot = gaPok + tjgIsSu + tjgAn
    ptg   = 1.0 / 100 * gaKot
    gaBer = gaKot - ptg
    print("Gaji Pokok               : Rp " + str(gaPok) + " ")
    print("Tunjangan Istri/Suami    : Rp " + str(tjgIsSu) + " ")
    print("Tunjangan Anak           : Rp " + str(tjgAn) + " ")
    print("--------------------------------------------------------" " + ")
    print("Gaji Kotor               : Rp " + str(gaKot) + " ")
    print("Potongan (1.0%)          : Rp " + str(ptg) + " ")
    print("--------------------------------------------------------" " - ")
    print("Gaji Bersih              : Rp " + str(gaBer) + " ")











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

