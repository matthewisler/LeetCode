import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    dist = employee.drop_duplicates(subset = 'salary')
    dist['rank'] = dist['salary'].rank(method='dense', ascending=False)
    ans = dist[dist['rank'] == 2][['salary']]
    ans.rename(columns={'salary': "SecondHighestSalary"}, inplace = True)
    if ans.empty:
        return pd.DataFrame({"SecondHighestSalary": [np.NaN]})
    return ans