def mun(player) :
    if 90 <= player >= 100 :
        return ("Naice klub mu memang terbaik, best club in the world")
    elif 80 <= player > 90 :
        return ("Nanggung banget kasih 90 lahh, kasih nilai segitu cocok e buat chelsea")
    else :
        return ("Nguawur kasih rating dikit banget, MU adalah klub terbaik boss,sekarang masih ngalah aja, makanya sering kalah")
while True :
    A = int(input("Rating performa manchester united musim ini 1-100 :"))
    print (mun(A))
    tanya = input("Mau rating lagi y/t :")
    if tanya == "t" :
        print("Oke makasi")
    break


