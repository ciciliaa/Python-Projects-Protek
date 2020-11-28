# script status berat badan

def statusBeratBadan(bb, tb):
    bmi = bb / (tb ** 2 / 100)
    return(bmi)

bb = float(input("Masukkan Berat Badan (kg) : "))
tb = float(input("Masukkan Tinggi Badan (cm) : "))
bmi = bb / (tb ** 2 / 100)
if (bmi < 18):
    print("Status berat badan anda KURUS")
elif (bmi >= 18) or (bmi < 23):
    print("Status berat badan anda IDEAL")
elif (bmi >= 23) or (bmi < 27):
    print("Status berat badan anda GEMUK")
elif (bmi >= 27) or (bmi < 35):
    print("Status berat badan anda OBESITAS")
elif (bmi >= 35):
    print("Status berat badan anda OBESITAS MORBID")

