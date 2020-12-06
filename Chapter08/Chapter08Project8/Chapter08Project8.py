def dictionary(buah):
    buah = {'apel' : 5000,
            'jeruk' : 8500,
            'mangga' : 7800,
            'duku' : 6500}
        
    values = tuple(dictionary.values())
    hargaTermahal = max(values)
    indexHargaTermahal = values.index(hargaTermahal)
    print(indexHargaTermahal)


def rataHarga(buah):
    harga = list(buah.values())
    rata = sum(harga)/len(harga)
    return rata

print("Rata-rata harga buah: ")
