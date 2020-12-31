file = open("chapter10praktikum2.txt", "r")
buka = file.readlines()
dic = {}

for i in range(len(lines)):
    x = buka[i]
    displit = x.split("|")
    nim = displit[0]
    nama = displit[1]
    alamat = displit[2].replace("\n", "")

    dic = {"nim" : nim, "nama" : nama, "alamat" : alamat}

print(dic)
