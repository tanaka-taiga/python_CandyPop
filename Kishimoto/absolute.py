#引数を取得
import sys
args = sys.argv

num = int(args[1])
#絶対値取得関数
absolute_value = abs(num)

#結果出力
print(num," ",absolute_value,end="")