from datetime import date
from database import session
from mkdb_transport import transport

import sys
args = sys.argv

try:
    dates = args[1]
    seqs = args[2]
    departures = args[3]
    arrivals = args[4]
    vias = args[5]
    amounts = args[6]

    transport = transport(
        date = dates,
        seq = seqs,
        departure = departures,
        arrival = arrivals,
        via = vias,
        amount = amounts,
    )
    session.add(transport)
    session.commit()
except:
    print("error:交通費精算テーブルにデータを登録できませんでした")