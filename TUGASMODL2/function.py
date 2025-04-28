# Variabel global untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi Create
def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    data_mahasiswa.append(nama)
    print(f"{nama} telah ditambahkan.")

# Fungsi Read
def tampilkan_mahasiswa():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        print("Daftar Mahasiswa:")
        for i, nama in enumerate(data_mahasiswa, start=1):
            print(f"{i}. {nama}")

# Fungsi Update
def ubah_mahasiswa():
    tampilkan_mahasiswa()
    try:
        indeks = int(input("Masukkan indeks mahasiswa yang akan diubah: ")) 
        if 0 <= indeks < len(data_mahasiswa):
            nama_baru = input("Masukkan nama baru: ")
            data_mahasiswa[indeks] = nama_baru
            print("Data mahasiswa telah diperbarui.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# Fungsi Delete
def hapus_mahasiswa():
    tampilkan_mahasiswa()
    try:
        indeks = int(input("Masukkan indeks mahasiswa yang akan dihapus: ")) 
        if 0 <= indeks < len(data_mahasiswa):
            nama = data_mahasiswa.pop(indeks)
            print(f"{nama} telah dihapus dari daftar.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# Fungsi Menu
def tampilkan_menu():
    print("\nMenu:")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Mahasiswa")
    print("3. Ubah Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")

# Main loop
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            tambah_mahasiswa()
        elif pilihan == '2':
            tampilkan_mahasiswa()
        elif pilihan == '3':
            ubah_mahasiswa()
        elif pilihan == '4':
            hapus_mahasiswa()
        elif pilihan == '5':
            print("Keluar dari program.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")

# Jalankan program
main()