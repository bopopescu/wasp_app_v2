from ..database.model import get_table_item
import datetime

def make_portfolio(portfolio):
    items=[]
    for item in portfolio:
        a = get_table_item(item['product_id'])
        date_format = "%Y/%m/%d"
        s_date = datetime.datetime.strptime(a['p_start_d'], date_format)
        e_date = datetime.datetime.strptime(a['p_end_d'], date_format)
        delta = e_date - s_date
        a['product_duration'] = delta.days
        a['amount_purchase']=item['amount_purchase']
        a['receipt_no']=item['sales_id']
        items.append(a)
    return items

