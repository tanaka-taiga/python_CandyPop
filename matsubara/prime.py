import sys
args = sys.argv

primenum = int(args[1])

def calc_prime(num):
    sosulist = []
    for i in range(2, primenum+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            sosulist.append(i)
    return sosulist

def check_sosu(list,num):
    checker = False
    for i in range(0,len(list)-1):
        if(num % list[i] ==0):
            return True
        else:
            continue

checker = check_sosu(calc_prime(primenum),primenum)
if primenum >=1000:
    print("1000以上は判定できません",end="")
elif checker:
    print("not",end="")
else:
    print("Prime",end="")

