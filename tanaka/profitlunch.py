import sys
args = sys.argv

karaage = int(args[1])
curry = int(args[2])

# 売り上げを計算
karaage_sales = 760*karaage
curry_sales = 850*curry

total_sales = karaage_sales + curry_sales

#原価を計算
karaage_cost = round(karaage_sales * 0.323)
curry_cost = round(curry_sales * 0.284)

total_cost = karaage_cost + curry_cost

#粗利を計算
profit_karaage = karaage_sales - karaage_cost
profit_curry = curry_sales - curry_cost

total_profit = profit_karaage + profit_curry



print('売上高：{0}、原価：{1}、粗利：{2}'.format(total_sales,total_cost,total_profit),end="")