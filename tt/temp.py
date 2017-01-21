# 可以自己import我们平台支持的第三方python模块，比如pandas、numpy等。
import pandas as pd

# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    context.s1 = "000001.XSHE"
    # 是否已发送了order
    context.fired = False

# 你选择的证券的数据更新将会触发此段逻辑，例如日或分钟历史数据切片或者是实时数据切片更新
def handle_bar(context, bar_dict):
    # 开始编写你的主要的算法逻辑

    # bar_dict[order_book_id] 可以拿到某个证券的bar信息
    # context.portfolio 可以拿到现在的投资组合状态信息

    # 使用order_shares(id_or_ins, amount)方法进行落单

    df = pd.read_csv('data/000039.csv', index_col='date', parse_dates=True)
    today = str(context.now).split()[0]


    for date in df.index:
        date = str(date).split()[0]
        if date == today:
            se = df.loc[date]
            if se.type == 'buy':
                order_shares('000039.XSHE', se.quantity, style=LimitOrder(se.price))
            elif se.type == 'sell':
                order_shares('000039.XSHE', se.quantity, style=LimitOrder(se.price))
