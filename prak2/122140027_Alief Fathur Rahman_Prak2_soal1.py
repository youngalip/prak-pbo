class Mahasiswa :
    def __init__(self,nama,nim,angkatan,isMahasiswa):
        self.__nama = nama
        self.__nim = nim
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa
        
    def get_nama(self):
        return self.__nama
        
    def set_nama(self, nama):    
        self.__nama = nama
        
    def get_nim(self):
        return self.__nim
        
    def set_nim(self, nim):    
        self.__nim = nim
        
    def check_angkatan(self) :
        if self.angkatan == 2022 :
            return "INLINEER" # NAMA ANGKATAN
        else :
            return "Bukan INLINEER"
        
    def check_tingkatan(self):
        return 2024 - self.angkatan
        
    def check_status(self):
        if self.isMahasiswa:
            return "Aktif"
        else :
            return "Tidak Aktif"
            
mhs1 = Mahasiswa("Alief Fathur Rahman","122140027",2022,True)
print("Nama : ", mhs1.get_nama())
print("NIM : ", mhs1.get_nim())
print("Angkatan :", mhs1.check_angkatan())
print("Tingkat : ", mhs1.check_tingkatan())
print("Status : ", mhs1.check_status())

print()

mhs2 = Mahasiswa("Fitra Ilyasa", "120140001",2020,True)
print("Nama : ", mhs2.get_nama())
print("NIM : ", mhs2.get_nim())
print("Angkatan :", mhs2.check_angkatan())
print("Tingkat : ", mhs2.check_tingkatan())
print("Status : ", mhs2.check_status())