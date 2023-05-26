import sys
args = sys.argv

karaage = int(args[1])
curry = int(args[2])

karaage_sales = 760*karaage
curry_sales = 850*curry

total_sales = karaage_sales + curry_sales

print(total_sales,end="")