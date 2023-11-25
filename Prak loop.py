#Membuat Program loop menggunakan while serta input tinggi dan berat badan
while True:
  height = float(input("Masuk kan tinggi badan (cm):"))
  weight = float(input("Masuk kan berat badan (kg):"))

#Menghitung score BMI
  BMI = weight / (height / 100) ** 2

#Menulis persyaratan tinggi dan berat badan yang di input
  if  46 < height < 201 and 1 < weight < 151 :

#Output score BMI dan kategori
    print("Hasil score BMI anda adalah", BMI)
    if BMI < 18.5 :
       print ("Anda termasuk kategori : UNDERWEIGHT")
    elif  18.5  < BMI < 24.9 :
       print ("Anda termasuk kategori : NORMAL")
    elif 25 < BMI < 29.9 :
       print ("Anda termasuk kategori : OVERWEIGHT")
    elif 30 < BMI < 34.9 :
       print ("Anda termasuk kategori : OBESE")
    else :
       print ("Anda termasuk kategori : EXTREMLY OBESE")

#Menanyakan program akan dilanjutkan atau tidak    
    state = int(input("apakah ingin lanjut ? 0 = tidak, 1 = ya :"))

    if not state:
      print("Terima kasih telah menggunakan program BMI saya")
      break

#Jika tinggi dan berat badan yang di input tidak sesuai syarat
  else :
    print ("Tinggi atau berat badan yang di input salah")