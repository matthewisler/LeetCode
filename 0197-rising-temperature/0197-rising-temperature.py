import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')
    weather['PreviousTemperature'] = weather['temperature'].shift(1)
    weather['PreviousRecordDate'] = weather['recordDate'].shift(1)

    result = weather[
        (weather['temperature'] > weather['PreviousTemperature']) & 
        (weather['recordDate'] == weather['PreviousRecordDate'] + pd.Timedelta(days=1))
    ][['id']].rename(columns={'id': 'Id'})

    return result