
name_list = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]
kekka_list = []

for i in range(9):
    if i % 2 != 0:
       
        kekka_list.append(name_list[i])

print (kekka_list,end="")