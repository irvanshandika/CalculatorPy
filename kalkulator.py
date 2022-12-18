# Meminta input operasi dari pengguna
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
operasi = input("Masukkan operasi yang ingin Anda lakukan : ")

# Meminta input bilangan pertama dari pengguna
bilangan1 = float(input("Masukkan bilangan pertama: "))

# Meminta input bilangan kedua dari pengguna
bilangan2 = float(input("Masukkan bilangan kedua: "))

# Menentukan hasil berdasarkan operasi yang dipilih
if operasi == '1':
  hasil = bilangan1 + bilangan2
elif operasi == '2':
  hasil = bilangan1 - bilangan2
elif operasi == '3':
  hasil = bilangan1 * bilangan2
elif operasi == '4':
  hasil = bilangan1 / bilangan2
else:
  print("Operasi yang Anda masukkan tidak valid.")

# Menampilkan hasil ke layar
print("Hasil:", hasil)
