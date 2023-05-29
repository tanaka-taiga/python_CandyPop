#引数を取得
import sys
args = sys.argv

num = int(args[1])

if num <= 1:
    print("not",end="")
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("not",end="")
            break
    else:
        print("Prime",end="")