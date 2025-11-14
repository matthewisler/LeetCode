import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = accounts[accounts['income'] < 20000]
    average_salary = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)]
    high_salary = accounts[accounts['income'] > 50000]

    low_count = len(low_salary['account_id'])
    average_count = len(average_salary['account_id'])
    high_count = len(high_salary['account_id'])

    df = pd.DataFrame({'category': ["Low Salary", 'Average Salary', 'High Salary'],
                        "accounts_count": [low_count, average_count, high_count]
                    })
    return df