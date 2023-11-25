#Input operator yang dipilih
operator = str(input("select the oprator  multiplication, division, modulus, exponentiation : "))

#Input angka
A = int(input("angka 1 : "))
B = int(input("angka 2 : "))

#If and elif
if operator == 'multiplication' :
    res = A * B
elif operator == 'division' :
    res = A / B
elif operator == 'modulus' :
    res = A % B
elif operator == 'exponentiation' :
    res = A ** B

#Print program
print (f"{operator} from {A} and {B} is : {res} ")






