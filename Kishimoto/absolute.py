#引数を取得
import sys
args = sys.argv

num = int(args[1])
#絶対値取得
absolute_value = abs(num)

print(num,absolute_value,end="")