#引数を取得
import sys
args = sys.argv

#注文数入力
order_chicken  =  int(args[1])  
order_curry    =  int(args[2])  

#定価料金
price_chicken  =  760 
price_curry    =  850


total = order_chicken * price_chicken + order_curry * price_curry

print(total, end="")