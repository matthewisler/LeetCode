import pandas as pd

def find_maximum_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions.day = transactions.day.dt.date

    transactions['rnk'] = transactions.groupby('day')['amount'].rank(method = 'dense', ascending=False)

    return transactions[transactions.rnk == 1].iloc[:,[0]].sort_values('transaction_id')