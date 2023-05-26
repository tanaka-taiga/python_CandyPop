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
            sosulist.append()
    return sosulist

print(calc_prime(primenum),end="")