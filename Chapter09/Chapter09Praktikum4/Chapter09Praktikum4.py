def shuffleString(x, n):
    import random
    for i in range(5):
        strAcak = list("aku")
        gabung = ''.join(random.sample(strAcak, len(strAcak)))
        return(gabung)
    
    
print(shuffleString("aku", 5))
