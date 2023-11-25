#masukkan data
N = int(input("masukkan jumlah data:"))
data = []
for i in range (N) :
    data.append(input("Data ke {}:" . format(i + 1)))

#masukkan indeks awal dan akhir
print("")
while True :
    batas_atas = int(input("indeks awal:"))
    batas_bawah = int(input("indeks akhir:"))

#syarat indeks
    if batas_atas > batas_bawah :
        print("indeks awal harus lebih kecil dari indeks akhir ")
    elif batas_atas < 0 or batas_bawah < 0 :
        print("indeks harus positif")
    elif batas_bawah > len(data) :
        print("indeks melebihi panjang list")
#Cetak indeks
    else :
        print("")
        print(f"Data indeks ke {batas_atas} sampai dengan indeks ke {batas_bawah}")
        print(data[batas_atas : batas_bawah + 1])
# Pengulangan program
        state = input("mau lanjut apa tidak? (y/t)")
        if state == "t" :
            print ("Terima kasih ya")
            break

    



