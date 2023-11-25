# 1. Map ()
#Membuat program mengetahui akar dari data
angka = [4,16,49,400,441]
program = list(map(lambda x : x**0.5  , angka ))
print("akar akar:",program)

# 2. map()
#Membuat program mengubah suhu celcius ke farenheit
celcius = [14,25,26,74,26]
fahrenheit = list(map(lambda c : c * 9/5 + 32, celcius))
print("Suhu dalam fahrenheit:",fahrenheit)

# 1. Filter()
#Membuat program untuk mencari nilai yang remidi, yaitu yang dibawah 75
nilai = [90,98,78,86,75,70,60,66,52,48,71,74.5,74.9,100,78,89,85,74.98,0,12]
remidi = list(filter(lambda y : y < 75, nilai))
print("Nilai yang remidi:",remidi)

# 2. filter()
#Membuat program untuk mencari bilangan prima
def bil_prima(x) :
    if x < 2 :
        return False
    for i in range (2, int(x**0.5) + 1) :
        if x % i == 0 :
            return False
    return True

bilangan = [2,6,4,10,7,5,20,21,8,3]
prima = list(filter(bil_prima, bilangan))
print("Bilangan prima:", prima)

# 1. reduce()
#Import reduce
from functools import reduce
#Membuat program menggabungkan kata dengan tipe data string
kata = ["Manchester", " ", "United", " ", "is", " ", "The", " ", "best", " ", "club", " ", "in", " ",  "the", " ", "world"]
gabung = reduce(lambda a, b : a + b, kata) 
print("Kata Gabung:", gabung)

# 2. reduce()
#Membuat program mecari nilai maksimum dari data
nilai = [90,98,78,86,75,70,60,66,52,48,71,74.5,74.9,100,78,89,85,74.98,0,12]
maksimum = reduce(lambda x, y : x if x > y else y, nilai)
print("Nilai maksimum: ",maksimum )