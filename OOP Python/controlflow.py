# logika jika toyota urutan pertama 
mobil = ["toyota" , "mercedes" , "avanza" , "xenia"]
if mobil[0] == "toyota":
    print("mobil pertama adalah toyota")
elif mobil[0] == "mercedes":
    print("mobil pertama adalah mercedes")
elif mobil[0] == "avanza":
    print("mobil pertama adalah avanza")
elif mobil[0] == "xenia":
    print("mobil pertama adalah xenia")
else:
    print("mobil pertama tidak ditemukan")

# logika jika ada mobil mercedes

if "mercedes" in mobil:
    print("ada mobil mercedes")
else:
    print("tidak ada mobil mercedes")

    #logika mencari mobil yang ada dalam list mobil

mobil2 = input("cari mobil yang ada dalam list : ")
try: 
    user_input = str(mobil2)
    
except ValueError:
    print("Input yang dimasukkan bukan string")
    
if user_input in mobil:
    print("ada mobil " + user_input)

else:
    print("tidak ada mobil " + user_input)


    #switch case tidak ada digantikan dengan if else / dictionary 

def opsi_1():
    return "anda memilih toyota"

def opsi_2():
    return "Anda memilih mercedes"

def opsi_3():
    return "Anda memilih avanza"
def opsi_4():
    return "Anda memilih xenia"

def default_opsi():
    return "Opsi tidak valid"


# Dictionary sebagai implementasi switch-case
switch_dict = {
    "1": opsi_1,
    "2": opsi_2,
    "3": opsi_3,
    "4": opsi_4
}

# Input dari pengguna
user_input = input("Pilih toyota , mercedes , avanza , xenia (1, 2, 3 , 4): ")

# Menjalankan fungsi yang sesuai dengan input
result = switch_dict.get(user_input, default_opsi)()  # `get` mengembalikan fungsi default jika key tidak ditemukan
print(result)
  
