def isPythagoras(a,b,c):
    if (c * c == a * a - b * b) or (c * c == a * a + b * b):
        print(True)
    else :
        print(False)


isPythagoras(3,4,5)
isPythagoras(5,9,12)
isPythagoras(8,6,10)
isPythagoras(7,8,11)
