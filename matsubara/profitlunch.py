import sys
from decimal import Decimal, ROUND_HALF_UP
args = sys.argv

chicken_value = int(args[1])
carry_value = int(args[2])

gen_chicken = 0.323
gen_carry = 0.284

chicken_fee = 760
carry_fee = 850

def totalfee(chi,car):
    sum = chi * chicken_fee + car * carry_fee
    return sum

def genfee(chi,car):
    gensum = chi * chicken_fee *gen_chicken +car * carry_fee * gen_carry
    return gensum

def arafee(chi,car):
    arasum = totalfee(chi,car) - genfee(chi,car)
    return arasum

text ="売上高：" + str(totalfee(chicken_value,carry_value)) +"、原価：" +str(genfee(chicken_value,carry_value)) + "、粗利：" + str(arafee(chicken_value,carry_value))
print(text,end="")