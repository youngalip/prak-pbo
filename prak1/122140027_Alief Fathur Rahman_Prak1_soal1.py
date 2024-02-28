lower = int(input("Masukkan batas bawah: "))
upper = int(input("Masukkan batas atas: "))
total = 0

if lower < 0 or upper < 0 :
    print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
else :    
    for i in range(lower, upper):
        if i % 2 == 1:
            print(i)
            total += i
    print("Total :",total)