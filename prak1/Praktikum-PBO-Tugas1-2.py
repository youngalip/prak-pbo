r = int(input("Jari-Jari : "))
phi = 3.14
luas = phi * r * r
keliling = 2 * phi * r

if r < 0 :
    print("jari-jari lingkarang tidak boleh negatif")
else :
    print("Luas :",luas)
    print("Keliling :",keliling)