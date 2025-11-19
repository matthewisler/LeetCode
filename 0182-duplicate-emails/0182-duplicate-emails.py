import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person.groupby('email').count().reset_index()
    df = df[df['id']>1]
    df = df.rename(columns={"email":"Email"})
    return df['Email'].to_frame()