# Inisialisasi dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

# Input jumlah mahasiswa
jumlah = int(input("Masukkan jumlah mahasiswa: "))

# Input data setiap mahasiswa
for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nim = input("NIM: ")
    nama = input("Nama: ")

    # Input mata kuliah dan nilai (minimal satu, boleh lebih)
    mata_kuliah = []
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
    
    for j in range(jumlah_matkul):
        mk = input(f"  Nama Mata Kuliah ke-{j+1}: ")
        while True:
            try:
                nilai = float(input(f"  Nilai untuk {mk}: "))
                break
            except ValueError:
                print("  ⚠ Masukkan angka sebagai nilai.")
        mata_kuliah.append((mk, nilai))

    # Simpan data ke dalam dictionary
    data_mahasiswa[nim] = {
        'nama': nama,
        'nilai': mata_kuliah
    }

# Tampilkan seluruh data mahasiswa
print("\n📋 Daftar Seluruh Data Mahasiswa:")
print("-" * 60)
print("NIM\t\tNama\t\tMata Kuliah & Nilai")
print("-" * 60)
for nim, info in data_mahasiswa.items():
    print(f"{nim}\t{info['nama']}")
    for mk, nilai in info['nilai']:
        print(f"\t\t\t{mk}: {nilai}")
    print()

# Tampilkan rata-rata nilai tiap mahasiswa
print("\n📊 Nilai Rata-Rata Mahasiswa:")
print("-" * 60)
for nim, info in data_mahasiswa.items():
    nilai_list = [nilai for _, nilai in info['nilai']]
    rata2 = sum(nilai_list) / len(nilai_list)
    print(f"{info['nama']} (NIM: {nim}) -> Rata-rata: {rata2:.2f}")