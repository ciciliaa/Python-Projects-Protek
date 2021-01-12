from datetime import*

def diffDate(x):
    tgl = x.split("-")
    tanggal = []

    for x in tgl:
        tanggal.append(int(x))
        
        ygDipanggil = date(yyyy, mm, dd)
        sekarang = datetime.date(datetime.now())

        jumlah = sekarang - ygDipanggil
        return jumlah

diffDate(2021-1-1)
print("Selisih hari {0} dengan hari {1}".format(diffDate(2021-1-1)))
