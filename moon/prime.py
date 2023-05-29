import sys

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 ==0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# 引数数を取得し
num = int(sys.argv[1])

# 数が1000以下であるかを確認し、1000以下の場合は素数かどうかを判定
if num >= 1000:
    print("1000以上は判定できません",end="")
else:
    if is_prime(num):
        print("Prime",end="")
    else:
        print("not",end="")