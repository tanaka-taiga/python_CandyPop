import sys

def calculate_sales(karaage_orders, curry_orders):
    karaage_price = 760
    curry_price = 850

    total_sales = karaage_orders * karaage_price + curry_orders * curry_price
    return total_sales

# コマンドライン引数から注文数を取得
karaage_orders = int(sys.argv[1])
curry_orders = int(sys.argv[2])

# 売上高を計算
sales = calculate_sales(karaage_orders, curry_orders)

# 結果を表示
print(sales,end="")
