def print_odd_indexed_elements():
    names = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]
    odd_indexed_names = names[1::2] # 1から始まるインデックスを2つ飛ばしで取得
    print(odd_indexed_names,end='')
    
print_odd_indexed_elements()