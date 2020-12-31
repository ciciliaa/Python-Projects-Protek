file = open("chapter10praktikum5", "r")
for i in file:
    splitbil = bilangan.split("|")
    tambah = int(splitbil[0]) + int(splitbil[1])
    result.append(tambah)

file.close()
