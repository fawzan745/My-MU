# Buat list kosong
list = []

# Nama program
print("Program untuk mengurutkan bilangan bulat sesuai dengan input user")

# Loop utama
while True:

    # Minta user untuk memilih metode pengurutan
    metode_mengurutkan = int(input("Pilih metode mengurutkan (1: Ascending atau 2: Descending): "))

    # Urutkan list bilangan bulat
    if metode_mengurutkan == 1:
        break            
    elif metode_mengurutkan == 2:
        break
    else :
        print("Anda memasukkan metode diluar pilihan")

# Minta user untuk memasukkan bilangan bulat
while True:
        bilangan_bulat = int(input("Masukkan bilangan bulat: "))
        list.append(bilangan_bulat)

 # Urutkan list bilangan bulat
        if metode_mengurutkan == 1:
            # Urutkan secara ascending
            for i in range(len(list) - 1):
                for j in range(i + 1, len(list)):
                    if list[i] > list[j]:
                        list[i], list[j] = list[j], list[i]        
        elif metode_mengurutkan == 2:
            # Urutkan secara descending
            for i in range(len(list) - 1):
                for j in range(i + 1, len(list)):
                    if list[i] < list[j]:
                        list[i], list[j] = list[j], list[i]
        # Cetak list bilangan bulat yang telah diurutkan
        print(list)

        # Tanyakan apakah user ingin memasukkan bilangan bulat lagi
        bertanya = input("Masih ada bilangan yang ingin dimasukkan (y/t)? ")
        if bertanya == "t":
            break
print(list)