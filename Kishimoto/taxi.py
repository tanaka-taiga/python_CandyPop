#引数を取得
import sys
args = sys.argv

#距離変数
distance = int(args[1])

num = (distance - 1500) // 344
#運賃変数
fare = 0

if (distance >= 1500):
    fare = 630
    fare = (num * 98) + 630

print(fare,end="")