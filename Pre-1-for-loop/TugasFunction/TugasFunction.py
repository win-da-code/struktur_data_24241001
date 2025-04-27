# Variabel global untuk menyimpan data mahasiswa
mahasiswa = []

# Fungsi untuk menampilkan semua data mahasiswa
def show_data():
    if len(mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
    else:
        print("Daftar Mahasiswa:")
        for indeks, nama in enumerate(mahasiswa, start=1):  # Mulai dari 1
            print(f"{indeks}. {nama}")  # Tampilkan tanpa tanda kurung

# Fungsi untuk menambahkan data mahasiswa
def insert_data():
    nama_baru = input("Nama mahasiswa baru: ")
    mahasiswa.append(nama_baru)
    print(f"Data '{nama_baru}' berhasil ditambahkan.")

# Fungsi untuk mengedit data mahasiswa
def edit_data():
    show_data()
    try:
        indeks = int(input("Inputkan nomor mahasiswa yang akan diedit: ")) - 1
        if indeks < 0 or indeks >= len(mahasiswa):
            print("Nomor mahasiswa tidak ditemukan.")
        else:
            nama_baru = input("Nama baru: ")
            mahasiswa[indeks] = nama_baru
            print("Data berhasil diubah.")
    except ValueError:
        print("Input harus berupa angka.")

# Fungsi untuk menghapus data mahasiswa
def delete_data():
    show_data()
    try:
        indeks = int(input("Inputkan nomor mahasiswa yang akan dihapus: ")) - 1
        if indeks < 0 or indeks >= len(mahasiswa):
            print("Nomor mahasiswa tidak ditemukan.")
        else:
            print(f"Mahasiswa '{mahasiswa[indeks]}' berhasil dihapus.")
            del mahasiswa[indeks]
    except ValueError:
        print("Input harus berupa angka.")

# Fungsi untuk menampilkan menu
def show_menu():
    print("\n" + "-" * 10 + " MENU " + "-" * 10)
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[5] Keluar")

    try:
        menu = int(input("Pilih menu: "))
        print()
        if menu == 1:
            show_data()
        elif menu == 2:
            insert_data()
        elif menu == 3:
            edit_data()
        elif menu == 4:
            delete_data()
        elif menu == 5:
            print("Terima kasih! Program selesai.")
            exit()
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

# Program utama (main loop)
if __name__ == "__main__":
    while True:
        show_menu()
