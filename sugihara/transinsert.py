from datetime import date
from database import session
from transport_table import Transport
import sys

args = sys.argv
input1 = int(args[1])
input2 = str(args[2])
input3 = str(args[3])
input4 = str(args[4])
input5 = str(args[5])
input6 = int(args[6])

transport = Transport(
    data = input1,
    seq = input2,
    departure = input3,
    arrival = input4,
    via = input5,
    amount = input6
)
if(session.query(Transport.data).filter_by(data = input1).count() >= 1 and session.query(Transport.seq).filter_by(seq = input2).count() >= 1):
    print("error:交通費生産テーブルにデータを登録できませんでした")
session.add(transport)
session.commit()
#コミット