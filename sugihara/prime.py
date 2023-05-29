import sys #インポート
args = sys.argv

input1 = int(args[1])#引数を代入

#素数判定
def judgment_prime(input1):
    i = 2
    while(True):
        if(input1 == i):
            result = "Prime"
            break
        elif(input1 % i == 0):
            result = "not"
            break
        else:
            i = i + 1
    return result
    
#パフォーマンス処理
if(input1 >= 1000):
    print("1000以上は判定できません",end="")
else:
 print(judgment_prime(input1),end="")




