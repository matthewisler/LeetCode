import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    total_deliveries = len(delivery['delivery_id'])
    immediate_deliveries = delivery[delivery['order_date']==delivery['customer_pref_delivery_date']]
    percentage = round(100*(len(immediate_deliveries['delivery_id'])/total_deliveries) ,2)
    df = pd.DataFrame({"immediate_percentage": [percentage]})
    return df