# Judul Program
judul = "Aplikasi Kartu Seluler My MU"
print(judul.center(100))
print()

# Membuat Variable Menu isi pulsa
menu_pulsa = [20000, 50000, 100000, 200000]

#Membuat Variable Menu isi paket data
paket1 = "5GB"
paket2 = "10GB"
paket3 = "30GB"
paket4 = "40GB"
paket = [paket1 + "(35000)", paket2 + "(60000)" , paket3 + "(90000)", paket4 + "(120000)"]

# Membuat fungsi isi pulsa
def isi_pulsa(pulsa) :
    global Pulsa
    if pulsa == 1 :
        if MU_pay - 20000 > 0:
            print(f"Pulsa {menu_pulsa[0]} berhasil diisi")
            return Pulsa + 20000 
        else :
            print("Saldo MU pay anda tidak cukup, silahkan isi dulu")
    elif pulsa == 2 :
        if MU_pay - 50000 > 0:
            print(f"Pulsa {menu_pulsa[1]} berhasil diisi")
            return Pulsa + 50000
        else :
            print("Saldo MU pay anda tidak cukup, silahkan isi dulu")
    elif pulsa == 3 :
        if MU_pay - 100000 > 0 :
            print(f"Pulsa {menu_pulsa[2]} berhasil diisi")
            return Pulsa + 100000
        else :
            print("Saldo MU pay anda tidak cukup, silahkan isi dulu")
    elif pulsa == 4 : 
        if MU_pay - 200000 > 0 :
            print(f"Pulsa {menu_pulsa[3]} berhasil diisi")
            return Pulsa + 200.000
        else :
            print("Saldo MU pay anda tidak cukup, silahkan isi dulu")
    else :
        print("pilihan tidak tersedia di dalam menu")    

# Membuat fungsi isi paket data
def isi_paket_data(paket) :
    global Paket_Data
    if paket == 1 :
        if MU_pay - 35000 > 0:
            print(f"Paket Data {paket1} berhasil diisi")
            return Paket_Data.append(paket1)
        else :
            print("Saldo MU pay anda tidak cukup, silahkan isi dulu")
    elif paket == 2 :
        if MU_pay - 60000 > 0:
            print(f"Paket Data {paket2} berhasil diisi")
            return Paket_Data.append(paket2)
        else :
            print("Saldo MU pay anda tidak cukup, silahkan isi dulu")
    elif paket == 3 :
        if MU_pay - 90000 > 0:
            print(f"Paket Data {paket3} berhasil diisi")
            return Paket_Data.append(paket3)
        else :
            print("Saldo MU pay anda tidak cukup, silahkan isi dulu")
    elif paket == 4 :
        if MU_pay - 120000 > 0:
            print(f"Paket Data {paket4} berhasil diisi")
            return Paket_Data.append(paket4)
        else :
            print("Saldo MU pay anda tidak cukup, silahkan isi dulu")
    else :
        print("pilihan tidak tersedia di dalam menu")

# Membuat kalimat selamat datang
print("Selamat datang di My MU".center(100))
print()

# Membuat Variable untuk menyimpan saldo MU pay
saldo = int(input("Masukkan saldo MU pay yang anda miliki: "))
MU_pay = saldo

# Membuat Looping dengan While True
while True :
    # Membuat Variable untuk menyimpan setiap menu
    Pulsa = 0
    Paket_Data = []
    print("Sisa Pulsa, Paket data, dan Mu pay anda hari ini:")
    print("Pulsa =", Pulsa)
    print("Paket Data = ", *Paket_Data, sep="")
    print("MU pay =", MU_pay)

    print()

    # Membuat Menu Aktivitas
    print("Menu di My MU:")
    menu = ["Membeli Pulsa", "Membeli Paket Data"]
    for nomor, isi in enumerate(menu, start=1):
        print(f"{nomor}. {isi}")

    # Menginput Aktivitas
    aktivitas = int(input("Apa yang ingin anda lakukan hari ini (1-3):"))

    # Aktivitas yang dilakukan
    if aktivitas == 1 :
        for nomor, isi in enumerate(menu_pulsa, start=1):
            print(f"{nomor}. {isi}")
        tanya_pulsa = int(input("Menu pulsa mana yang ingin anda beli? "))
        Pulsa = isi_pulsa(tanya_pulsa)
    elif aktivitas == 2 :
        for nomor, isi in enumerate(paket, start=1):
            print(f"{nomor}. {isi}")
        tanya_paket = int(input("Menu paket mana yang ingin anda beli? "))
        isi_paket_data(tanya_paket)
    else :
        print("pilihan tidak tersedia di dalam menu")

    print()

    #Menampikan sisa saldo 
    print("Sisa Pulsa, Paket data, dan MU pay anda hari ini:")
    print("Pulsa =", Pulsa)
    print("Paket Data = ", *Paket_Data, sep="")
    print("MU pay =", MU_pay)
    print()

    tanya = input("Apakah anda ingin menggunakan layanan My MU lagi (y/t)? ")
    if tanya != "y" :
        #Menampilkan Pulsa, Paket Data, dan MU pay setelah transaksi
        print("Sisa Pulsa, Paket data, dan MU pay anda hari ini:")
        print("Pulsa =", Pulsa)
        print("Paket Data = ", *Paket_Data, sep="")
        print("MU pay =", MU_pay)
        print()
        print("Terima Kasih telah menggunakan layanan My MU🙏")
        print("Semoga hari mu menyenangkan dan MU menang terus")
        break

