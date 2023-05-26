import sys #インポート
args = sys.argv

input1 = int(args[1])#引数を代入

#パフォーマンス処理
if(input1 >= 1000):
    print("1000以上は判定できません")

#素数判定
def judgment_prime():
    i = 2
    while(True):
        if(input1 == i):
            result = "prime"
            break
        elif(input1 % i == 0):
            result = "not"
            break
        else:
            i = i + 1
    return result
    

print(judgment_prime())

