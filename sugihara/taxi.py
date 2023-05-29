import sys #インポート

args = sys.argv
input1 = int(args[1]) #引数を代入
price = 630

if(input1 > 1500): #条件処理
    count = (input1 -1500)//344 +1
    price = price +98 * count

print(price,end="") #料金出力