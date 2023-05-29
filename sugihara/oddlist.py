#リスト定義
name_list = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]
print_list = [] #出力用のリスト

#奇数の要素番号のデータを出力用のリストに追加
for i in range(len(name_list)):
    if(i % 2 == 1):
        print_list.append(name_list[i])
    else:
        pass
print(print_list,end="")