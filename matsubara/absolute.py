import sys
import math
args = sys.argv

# 引数をInt型に定義
input_num = int(args[1]) 

# 絶対値を返す関数(numが引数)
def absolute(num):
    return abs(num)

#出力
print(str(input_num) + " " + str(absolute(input_num)) , end= "")