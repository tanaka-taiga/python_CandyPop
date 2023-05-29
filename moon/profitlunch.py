import sys

def calculate_profit(karaage_orders, curry_orders):
    karaage_price = 760
    karaage_cost_rate = 32.3 / 100
    curry_price = 850
    curry_cost_rate = 28.4 / 100   
    
    karaage_sales = karaage_orders * karaage_price # 売上
    karaage_cost = round(karaage_sales * karaage_cost_rate) # 原価
    karaage_profit = karaage_sales - karaage_cost # 利益
    
    curry_sales = curry_orders * curry_price # 売上
    curry_cost = round(curry_sales * curry_cost_rate) # 原価
    curry_profit = curry_sales - curry_cost # 利益
    
    total_sales = karaage_sales + curry_sales # total 売上
    total_cost = karaage_cost + curry_cost # total 原価
    total_profit = karaage_profit + curry_profit # total 利益
    
    return total_sales, total_cost, total_profit    

# コマンドライン引数から注文数を取得
karaage_orders = int(sys.argv[1])
curry_orders = int(sys.argv[2])

# 売上、原価、利益を計算
sales, cost, profit = calculate_profit(karaage_orders, curry_orders)

# 結果を表示
print(f'売上高：{sales}、原価：{cost}、粗利：{profit}',end='')