import sys
args  =sys.argv

chicken_value = int(args[1])
carry_value = int(args[2])

chicken_fee = 760
carry_fee = 850

def totalfee(chicken,carry):
    sum = chicken * chicken_fee + carry * carry_fee
    return sum

print(totalfee(chicken_value,carry_value),end= "")