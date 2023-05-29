#引数を取得
import sys
args = sys.argv

#注文数入力
order_chicken  =  int(args[1])  
order_curry    =  int(args[2])  

#定価料金
price_chicken  =  760 
price_curry    =  850

#原価率
cost_rate_chicken   =   32.3
cost_rate_curry     =   28.4


#唐揚げ定食売り上げ
chicken_sales = order_chicken * price_chicken
#カレーセット売り上げ
curry_sales = order_curry * price_curry

#総合売り上げ
total_sales = chicken_sales + curry_sales

#原価
prime_cost_chicken  = round(chicken_sales * (cost_rate_chicken / 100))
prime_cost_curry    = round(curry_sales * (cost_rate_curry / 100))

#総合原価
total_prime_cost = prime_cost_chicken + prime_cost_curry

#粗利
gross_profit_chicken   =  chicken_sales - prime_cost_chicken
gross_profit_curry     =  curry_sales - prime_cost_curry

#総合粗利
total_gross_profit = gross_profit_chicken + gross_profit_curry

# print("売上高：",total_sales,"、","原価：",total_prime_cost,"、","粗利：",total_gross_profit ,end="")
print(f'売上高：{total_sales}、原価：{total_prime_cost}、粗利：{total_gross_profit}',end='')