#logika operasi matematika
print(5+5) # tambah
print(5-5) # kurang 
print(4/2) # bagi
print(4*2) # kali
print(4%2) # modulus
print(4**2) # pangkat

x = 5
y = 10
#hannya menghasilkan nilai true dan false saja 
print("x > y:", x > y) 
print("x < y:", x < y) 
print("x == y:", x == y)
print("x != y:", x != y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

#operasi logika
if (x < y) :
    print("x lebih kecil dari y")
else:
    print("x lebih besar dari y")


# Meminta input untuk angka pertama
angka1 = input("Masukkan angka pertama: ")

# Mengantisipasi jika input bukan angka atau mengandung koma
try: 
    user_nomer = float(angka1)
    print("Angka pertama adalah: " + str(user_nomer))
except ValueError:
    print("Input yang dimasukkan bukan angka.")
    user_nomer = 0
    # (try dan except digunakan untuk mengantisipasi kesalahan pada Python)

# Meminta input untuk angka kedua
angka2 = input("Masukkan angka kedua: ")

try:
    user_number = float(angka2)
    print("Angka kedua adalah: " + str(user_number))
except ValueError:
    print("Input yang dimasukkan bukan angka.")
    user_number = 0

# Operasi kalkulator
print("Hasil operasi tambah: " + str(user_nomer + user_number))
print("Hasil operasi kurang: " + str(user_nomer - user_number))
print("Hasil operasi bagi: " + str(user_nomer / user_number if user_number != 0 else "undefined"))  # user_number != 0 digunakan untuk mengantisipasi pembagian dengan angka 0
print("Hasil operasi kali: " + str(user_nomer * user_number))
print("Hasil operasi modulus: " + str(user_nomer % user_number if user_number != 0 else "undefined"))
print("Hasil operasi pangkat: " + str(user_nomer ** user_number))

# logika perbandingan 
if user_nomer < user_number:
    print("Angka pertama lebih kecil dari angka kedua.")
elif user_nomer > user_number:
    print("Angka pertama lebih besar dari angka kedua.")
else:
    print("Angka pertama sama dengan angka kedua.")
