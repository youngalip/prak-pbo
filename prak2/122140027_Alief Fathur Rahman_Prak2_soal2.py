class lowongan:
    def __init__(self, nama, umur, bidang, instagram = None):
        self.__nama = nama
        self.__umur = umur
        self.__bidang = bidang
        self.instagram = instagram
        self.file = None

    @property
    def nama(self):
        return self.__nama
        
    @property
    def umur(self):
        return self.__umur
        
    @property
    def bidang(self):
        return self.__bidang
    
    def __del__(self):
        if self.file:
            self.file.close()
            print(f"File untuk data pelamar {self.__nama} telah diinput")

    def tulis_ke_file(self):
        self.file = open('lowongan.txt', 'a')
        self.file.write(f"Nama: {self.__nama}, Umur: {self.__umur}, Bidang: {self.__bidang}\n")
        if self.instagram:
            self.file.write(f", Instagram: https://www.instagram.com/{self.instagram}/\n")
        else:
            pass
        
pelamar1 = lowongan("Alief", 20, "Koki","alief_fr")
print(pelamar1.nama)
print(pelamar1.umur)
print(pelamar1.bidang)
pelamar1.tulis_ke_file()    
del pelamar1

print()

pelamar2 = lowongan("Nasrul", 19, "Kasir")
print(pelamar2.nama)
print(pelamar2.umur)
print(pelamar2.bidang)
pelamar2.tulis_ke_file()
del pelamar2




