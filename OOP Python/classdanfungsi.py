
class Mobil: # disini saya membuat class Mobil

    def  __init__(self , merk , plat): # saya membuat constructor
        self.merk = merk
        self.plat = plat

merk = input("masukkan merk mobil:")
plat = int(input("masukkan nomor plat:"))

mobil1 = Mobil(merk, plat) # inisialisasi objek mobil1 dengan menggunakan class Mobil

print("mobil kamu adalah",mobil1.merk)
print("plat kamu adalah" ,mobil1.plat)

 # saya membuat class datadiri agar lebih memahami tentang class dan object
class datadiri:
     def __init__(a , nama , umur , alamat , pekerjaan): # a disini untuk inisialisasi 
         a.nama = nama
         a.umur = umur
         a.alamat = alamat
         a.pekerjaan = pekerjaan

nama = input("masukkan nama:")
umur = int(input("masukkan umur:"))
alamat = input("masukkan alamat:")
pekerjaan = input("masukkan pekerjaan:")

datadiri1 = datadiri(nama, umur, alamat, pekerjaan) # inisialisasi datadiri1 dengan menggunakan class datadiri
print("nama kamu adalah",datadiri1.nama , "umur kamu adalah", datadiri1.umur ,"kamu tiggal di ", datadiri1.alamat , "pekerjaan kamu adalah", datadiri1.pekerjaan)



#disini saya membuat fungsi perkalian berisikan variabel a dan b
def perkalian(a , b):
    hasil = a * b #memasukkan rumus aritmatika
    return hasil #mengembalikan nilai hasil 

a = int(input("masukkan angka pertama:")) 
b = int(input("masukkan angka kedua:")) 

print("hasil perkalian dari", a, "dan", b, "adalah", perkalian(a, b)) 

         



    
        
