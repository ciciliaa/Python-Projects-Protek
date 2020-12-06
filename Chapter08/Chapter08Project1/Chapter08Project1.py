try :
    bbul = []
    bil = int(input("Masukkan bilangan bulat: "))
    bbul.append(bil)
    i+= 1
except ValueError :
    print("Bukan bilangan bulat")
bbul.sort(reverse=True)
print(bbul)
