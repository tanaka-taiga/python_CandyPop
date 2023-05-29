import sys
import math
args = sys.argv

num = int(args[1])

# 素数を判定する関数
def isprime(N):
    if N < 2:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True

if num >= 1000:
    print("1000以上は判定できません",end="")
else:
    if isprime(num) == True:
        print("Prime",end="")
    if isprime(num) == False:
        print("not",end="")


    
        
        