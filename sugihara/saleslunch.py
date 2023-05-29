import sys #インポート
args = sys.argv

input1 = int(args[1])#引数を代入

input2 = int(args[2])

#料金定義
karaage_set_meal = 760
curry_set = 850

price = karaage_set_meal * input1 + curry_set * input2 #料金計算

print(price)