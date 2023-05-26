import sys
args = sys.argv

kyori = args[1]
kyori = int(kyori)

if kyori <= 1500:
    pay = 630
else:
    kyori_o1500 = kyori-1500
    pay = 630 + ((kyori_o1500//344)+ 1) *98

print(pay,end="")