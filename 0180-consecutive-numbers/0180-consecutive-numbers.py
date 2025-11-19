import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs = logs.sort_values("id").reset_index(drop=True)
    same_three = (
        (logs["num"] == logs["num"].shift(1)) &
        (logs["num"] == logs["num"].shift(2))
    )
    result = (
        logs.loc[same_three, "num"]
        .drop_duplicates()
        .reset_index(drop=True)
        .to_frame(name="ConsecutiveNums")
    )
    return result