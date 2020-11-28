# script jarak mobil

def kasusJarakMobil(v0, a):
    jarak = v0 * t + 1/2 * a * t ** 2
    return jarak

v0 = float(input("Masukkan kecepatan mula-mula = "))
a = float(input("Masukkan percepatan = "))
t = 0
while (t < 10):
    t += 1
    jarak = v0 * t + 1/2 * a * t ** 2
    print("t = ", t, "", "", "", " (S(t) = " + str(jarak) + ")")
t += 1
