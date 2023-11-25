angka = []
for i in [21,3,68] :
    for a in [745, 264, 414, 245] :
        angka.append(i + a)
print (angka)


angka_1 = [i+a for i in [21,3,68] for a in [745,264,414,245]]
print (angka_1)