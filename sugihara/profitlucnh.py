import sys #インポート
args = sys.argv

input1 = int(args[1])#引数を代入
input2 = int(args[2])

#料金定義
karaage_set_meal = 760
curry_set = 850

#料金計算
karaage_price = karaage_set_meal * input1 
curry_price = curry_set * input2 
sum_price = karaage_price + curry_price

#原価計算
karaage_cost = round(karaage_price * 0.323)
curry_cost = round(curry_price * 0.284)
sum_cost = karaage_cost + curry_cost

#粗利計算
karaage_incom = karaage_price - karaage_cost
curry_incom = curry_price - curry_cost
sum_incom = karaage_incom + curry_incom


print(f"売上高：{sum_price}、原価：{sum_cost}、粗利：{sum_incom}",end="")