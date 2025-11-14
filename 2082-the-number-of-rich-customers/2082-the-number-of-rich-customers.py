import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    rich_customers = store[store['amount'] > 500]
    rich_count = len(set(rich_customers['customer_id']))
    ret = pd.DataFrame({"rich_count": [rich_count]})
    return ret