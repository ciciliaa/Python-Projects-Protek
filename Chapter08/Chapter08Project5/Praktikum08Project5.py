def kuadrat(bil):
    bilbul = [1, 3, 4, 6, 8, 9, 10]
    for i in range(bilbul):
        kali = bilbul[i] * bilbul[i]
        bilbul.append(kali)
        return bilbul
    
bilbul = [1, 3, 4, 6, 8, 9, 10]
hasil = kuadrat(bilbul)
print(hasil)
    
