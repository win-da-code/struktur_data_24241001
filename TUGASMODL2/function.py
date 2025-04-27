# Global variable untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menambah data (Create)
def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    data_mahasiswa.append(nama)
    print("Data berhasil ditambahkan.")

# Fungsi untuk menampilkan data (Read)
def tampilkan_mahasiswa():
    if not data_mahasiswa:
        print("Data mahasiswa kosong.")
    else:
        print("Daftar Mahasiswa:")
        for i, nama in enumerate(data_mahasiswa):
            print(f"{i}. {nama}")

# Fungsi untuk mengubah data (Update)
def ubah_mahasiswa():
    tampilkan_mahasiswa()
    try:
        indeks = int(input("Masukkan indeks mahasiswa yang ingin diubah: "))
        if 0 <= indeks < len(data_mahasiswa):
            nama_baru = input("Masukkan nama baru: ")
            data_mahasiswa[indeks] = nama_baru
            print("Data berhasil diubah.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# Fungsi untuk menghapus data (Delete)
def hapus_mahasiswa():
    tampilkan_mahasiswa()
    try:
        indeks = int(input("Masukkan indeks mahasiswa yang ingin dihapus: "))
        if 0 <= indeks < len(data_mahasiswa):
            data_mahasiswa.pop(indeks)
            print("Data berhasil dihapus.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# Fungsi untuk menampilkan menu
def show_menu():
    print("\n=== Menu ===")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Mahasiswa")
    print("3. Ubah Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_mahasiswa()
    elif pilihan == "2":
        tampilkan_mahasiswa()
    elif pilihan == "3":
        ubah_mahasiswa()
    elif pilihan == "4":
        hapus_mahasiswa()
    elif pilihan == "5":
        print("Keluar dari program...")
        exit()
    else:
        print("Pilihan tidak valid.")

# Main loop
while True:
    show_menu()