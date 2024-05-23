class Laci:
    def __init__(self):
        self.tumpukan = []
    
    def tambah_berkas(self, berkas):
        self.tumpukan.append(berkas)
        print(f"Berkas '{berkas}' ditambahkan ke dalam laci.")
        
    def keluarkan_berkas(self):
        if self.is_empty():
            raise Exception("Laci kosong. Tidak ada berkas yang bisa dikeluarkan.")
        berkas = self.tumpukan.pop()
        print(f"Berkas '{berkas}' dikeluarkan dari laci.")
        return berkas
    
    def berkas_teratas(self):
        if self.is_empty():
            raise Exception("Laci kosong. Tidak ada berkas di bagian atas.")
        return self.tumpukan[-1]

    def is_empty(self):
        return len(self.tumpukan) == 0

laci = Laci()

def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah berkas")
        print("2. Keluarkan berkas")
        print("3. Lihat berkas teratas")
        print("4. Keluar")
        
        pilihan = input("Pilih tindakan (1-4): ")

        if pilihan == '1':
            berkas = input("Masukkan nama berkas: ")
            laci.tambah_berkas(berkas)
        elif pilihan == '2':
            try:
                laci.keluarkan_berkas()
            except Exception as e:
                print(e)
        elif pilihan == '3':
            try:
                print(f"Berkas teratas adalah: {laci.berkas_teratas()}")
            except Exception as e:
                print(e)
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()