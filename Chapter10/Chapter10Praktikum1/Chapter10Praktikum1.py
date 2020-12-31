file = open("chapter10praktikum1.txt", "r")
bilangan = file.readlines()

genap = []
ganjil = []

for r in range(len(bilngan)):
    num = bilangan[r]

    if (int(num)) == 0:
        genap = genap + [num]
    else :
        ganjil = ganjil + [num]

print("Banyaknya bilangan genap : ", len(genap))
print("Banyaknya bilangan ganjil : ", len(ganjil))
