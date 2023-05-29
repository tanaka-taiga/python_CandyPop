import sys #インポート
args = sys.argv

input1 = int(args[1])#引数を代入

result = abs(input1)#絶対値の計算


print(str(input1)+" "+str(result),end="")#結果を出力
