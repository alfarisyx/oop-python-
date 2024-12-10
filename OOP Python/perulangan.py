# while dalam python 
# while loop untuk menampilkan angka 1 sampai 5 
i = 1
while i <= 10:
    print(i)
    i += 1
    
#jika i adalah 3
i = 1 
while i <= 10:
    print(i)
    if i == 3:
        break
    i += 1
    

  
i = 1 
while i <= 5: # kondisi untuk memastikan loop berjalan dari 1 hingga `i` mencapai 5
    print("*" * i)  # mendifinisikan variable string *  dikali i
    i += 1  # menambahkan nilai `i`
    
i = 5
while i > 0:  # Kondisi untuk memastikan loop berjalan hingga `i` mencapai 0
    print("*" * i)
    i -= 1  # Mengurangi nilai `i` secara bertahap
  
#memasukkan angika kemudian di looping

z = int(input("masukkan angka : "))
while z <= 10: # jika lebih dari 10 maka akan berhenti dan jika masukkan angka yang lebih dari 10 maka tidak ada loopingan 
    print(z * z)
    z += 1
    
# forloop 
    
buah = ["apel , pisang , semangka"] # loopingan untuk menampilkan buah
for x in buah :
    print(x)    
    
for y in "apel": # loopingan untuk menampilkan huruf apel
    print(y)
    

for z in range(6): 
    print("*" * z)  # menampilkan * sebannyak 6 baris yang muncul 5 karena * kali 0 = 0 (tidak muncul ) (0,1,2,3,4,5)
    
for d in range(5,0,-1): # loopingan untuk menampilkan angka dari 5 ke 1 start = 5 , stop = 0, step = -1
    print("*" * d)
    
    buah = ["apel" , "pisang" , "semangka"] # loopingan untuk buah jika buah adalah apel maka akan dilewati
    for a in buah :
        if a == "apel":
            continue
        print(a)
        
    buah = ["apel" , "pisang" , "semangka"] # loopingan untuk buah jika buah adalah pisang maka akan berhenti
    for s in buah :
        if s == "pisang":
            break 
        print(s)
        
        for q in range(2 , 30 ,3): #start = 2 , stop = 30 , step = 3
            print(q)
        
        # do while pada python 

while True:
    # Blok kode yang akan dijalankan
    user_input = input("Tekan 'y' untuk terus atau 'n' untuk keluar: ")
    
    # Kondisi untuk berhenti dari loop
    if user_input.lower() == 'n':
        print("Keluar dari loop.")
        break
    else:
        print("Melakukan operasi loop lagi...")
        
    
    
    