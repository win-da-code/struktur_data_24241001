tinggi = 3
for i in range(tinggi):
    bintang = '*' * (2 * i + 1)  # hanya ganjil: 1, 3, 5, ...
    spasi = ' ' * (tinggi - i - 1)
    print(spasi + bintang)