mhs = ["K001 : ROSIHAN ARI : 1979-09-01 : SOLO",
       "K002 : DWI AMALIA FITRIANI : 1979-09-17 : KUDUS",
       "K003 : FAZA FAUZAN : 2005-01-28 : KARANGANYAR",]

print("==========================================================================")
print("NIM".ljust(10, " "), "NAMA MAHASISWA".ljust(15, " "), "TGL LAHIR".ljust(15, " "), "TEMPAT LAHIR".ljust(15, " "))
print("--------------------------------------------------------------------------")

for data in mhs:
    dataList = data.split(",")
    nim = dataList[0]
    namaMahasiswa = dataList[1]
    tglLahir = dataList[2]
    dataTglLahir = tglLahir.split("-")
    tempatLahir = dataList[3]

    print(data["nim"].ljust(10, " "), data["namaMahasiswa"].ljust(18, " "), str(data["tglLahir"]).ljust(10, " "), data["tempatLahir"].ljust(10, " "))
    
