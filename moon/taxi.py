import sys,math

distance = sys.argv[1]

base_distance = 1500
base_fee = 630
extra_fee = 98
extra_distance = 344
total_fee = 0

# 1600               1500
if int(distance) <= base_distance:
    total_fee = base_fee
else:
    # 100
    distance_over = int(distance) - base_distance 
    # 1
    extra_fee_times = math.ceil(distance_over / extra_distance)
    # 630 + 98(+1,2)
    print(extra_fee_times)
    total_fee = base_fee + extra_fee_times * extra_fee

print(total_fee,end="")


