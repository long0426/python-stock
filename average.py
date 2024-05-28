import twstock as t
import pandas as p
import plotly.graph_objects as g

stock = t.Stock('0050')
date = stock.date
price = stock.price
data = p.DataFrame({'日期':date, '收盤價':price})

five = date[4:]
average = stock.moving_average(price, 5)
ma5 = p.DataFrame({'日期':five, '5日平均價格':average})

ten = date[9:]
average = stock.moving_average(price, 10)
ma10 = p.DataFrame({'日期':ten, '10日平均價格':average})

twenty = date[19:]
average = stock.moving_average(price, 20)
ma20 = p.DataFrame({'日期':twenty, '20日平均價格':average})

result = g.Figure()

result.add_trace(
    g.Scatter(
        x=data['日期'],
        y=data['收盤價'],
        name='收盤價'
    )
)

result.add_trace(
    g.Scatter(
        x=ma5['日期'],
        y=ma5['5日平均價格'],
        name='5日均價線'
    )
)

# result.show()

result.add_trace(
    g.Scatter(
        x=ma10['日期'],
        y=ma10['10日平均價格'],
        name='10日均價線'
    )
)

# result.show()

result.add_trace(
    g.Scatter(
        x=ma20['日期'],
        y=ma20['20日平均價格'],
        name='20日均價線'
    )
)

result.show()
