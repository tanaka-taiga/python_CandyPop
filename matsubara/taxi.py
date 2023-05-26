import sys
args = sys.argv

distance = int(args[1])

# 各料金設定
first_dis = 1500 # 初乗り距離
first_fee = 630 # 初乗り料金

# more_disメートル毎にmore_fee上がる
more_dis = 344 
more_fee =98 

def taxi_fee(dis):
    if(dis < first_dis):
        return first_fee
    elif(dis >=first_dis):
        over_first_d = dis - first_dis
        over_fee = over_first_d //more_dis + 1
        total_fee = over_fee * more_fee + first_fee 
        return total_fee

print(taxi_fee(distance),end ="")