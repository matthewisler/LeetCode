import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    idx = activity.groupby('player_id')['event_date'].idxmin()
    result = activity.loc[idx]
    return result[['player_id','device_id']]