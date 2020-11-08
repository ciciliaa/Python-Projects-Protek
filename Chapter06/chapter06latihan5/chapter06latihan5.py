# script mencari rata-rata, nilai maksimal, nilai minimal 5a
print("Mencari rata-rata, nilai maksimal, dan nilai minimal dari data : 5, 10, 4, 9, 30, 16, 2, 11 ")
list_angka = (5, 10, 4, 9, 30, 16, 2, 11)
daftar_angka = [int(x) for x in list_angka]

jumlah = 0
for angka in daftar_angka:
    jumlah += angka
rata_rata = jumlah / len(daftar_angka)

print("Nilai rata - rata :{}". format(rata_rata))
print("Nilai maksimal :{}". format(max(daftar_angka)))
print("Nilai minimal :{}". format(min(daftar_angka)))




# script mencari rata-rata, nilai maksimal, nilai minimal 5b
print("Mencari rata-rata, nilai maksimal, dan nilai minimal dari data : 81, 98, 12, 83, 45, 77, 69, 30, 56 ")
list_angka = (81, 98, 12, 83, 45, 77, 69, 30, 56)
daftar_angka = [int(x) for x in list_angka]

jumlah = 0
for angka in daftar_angka:
    jumlah += angka
rata_rata = jumlah / len(daftar_angka)

print("Nilai rata - rata :{}". format(rata_rata))
print("Nilai maksimal :{}". format(max(daftar_angka)))
print("Nilai minimal :{}". format(min(daftar_angka)))

