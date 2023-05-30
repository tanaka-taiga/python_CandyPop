from datetime import date
from database import session
from mkdb_transport import transport

import json
import sys
args = sys.argv

file_name = args[1]

transport_list = session.query(transport).all()

with open("../../files/"+ file_name, "w") as fp:
        json.dump(transport_list,fp)

# for i in transport_list:
#     dates = i.date
#     seqs = i.seq
#     departures = i.departure
#     arrivals = i.arrival
#     vias = i.via
#     amounts = i.amount

    
    # i_list = [dates,seqs, departures,arrivals, vias,amounts]

     #ファイルを開く
    # output_file = open("../../files/"+ file_name, mode="w", encoding="utf-8")

    # #ファイルに書き込む
    # output_file.writelines(str(i_list))

    # #ファイルを閉じる
    # output_file.close()