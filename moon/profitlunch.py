import sys

def calculate_profit(karaage_orders, curry_orders):
    karaage_price = 760
    karaage_cost_rate = 32.3 / 100
    curry_price = 850
    curry_cost_rate = 28.4 / 100   

# コマンドライン引数から注文数を取得
karaage_orders = int(sys.argv[1])
curry_orders = int(sys.argv[2])
