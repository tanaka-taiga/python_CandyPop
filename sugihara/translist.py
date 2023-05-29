import os
import sys
from database import session
from transport_table import Transport

args = sys.argv
input1 = str(args[1])

path = os.path.join(".","output",input1)

text_list = session.query(Transport).all()


transform = open(path,mode="w",encoding="utf-8")
for i in text_list:
    transform.write(f'"{i.data}","{i.seq}","{i.departure}","{i.arrival}","{i.via}","{i.amount}"\n')

transform.close()
#ファイルをとじる
