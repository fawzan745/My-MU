def hitung_point(w, d, l) :
    #Rumus menghitung point
    return lambda x : (x*w) + d + (l*0)

print("Program Menghitung Point Klub")
#Menginput setiap jumlah w,d,l
W = int(input("Jumlah kemenangan klub anda musim ini:"))
D = int(input("Jumlah seri klub anda musim ini:"))
L = int(input("Jumlah kekalahan klub anda musim ini:"))

#Memasukkan input dari user ke dalam fungsi
Point = hitung_point(W, D, L)

#Mencetak program
print ("Jumlah point klub samian adalah", Point(3)) 
