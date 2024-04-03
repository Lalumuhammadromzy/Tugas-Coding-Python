print("=="*25)
print(" INPUTKAN DATA DAN NILAI ".center(50,"-"))
print("=="*25)
nama = input("Masukkan Nama = ")
nim = input("Masukkan NIM = ")
prodi = input("Masukkan Prodi = ")
absen = int(input("Masukkan Nilai Absen = "))
uts = int(input("Masukkan Nilai UTS = "))
uas = int(input("Masukkan Nilai UAS = "))
nilai_batas = 60
jumlah = absen + uts + uas
rata_rata = jumlah/3
print("Jumlah Niai = ",jumlah)
print("Jumlah Nilai = ",rata_rata)
print("=="*25)
print("Nama Mahasiswa ".ljust(25) + ":",nama)
print("NIM Mahasiswa ".ljust(25) + ":",nim)
print("Prodi Mahasiswa ".ljust(25) + ":",prodi)
if rata_rata <=100 and rata_rata >= 95:
    print("Nilai Mahasiswa ".ljust(25) + ": A+ ",rata_rata)
elif rata_rata <=94 and rata_rata >= 90:
    print("Nilai Mahasiswa ".ljust(25) + ": A ",rata_rata)
elif rata_rata <= 89 and rata_rata >= 85:
    print("Nilai Mahasiswa ".ljust(25) + ": A- ",rata_rata)
elif rata_rata <= 84 and rata_rata>= 80:
    print("Nilai Mahasiswa ".ljust(25) + ": B+ ",rata_rata)
elif rata_rata <= 79 and rata_rata>= 75:
    print("Nilai Mahasiswa ".ljust(25) + ": B ",rata_rata)
elif rata_rata <= 74 and rata_rata >= 65:
    print("Nilai Mahasiswa ".ljust(25) + ": C ",rata_rata)
elif rata_rata <= 64 and rata_rata >= 55:
    print("Nilai Mahasiswa ".ljust(25) + ": E ",rata_rata)
else :
    print("Nilai Mahasiswa ".ljust(25) + ": F",rata_rata)
print("=="*25)