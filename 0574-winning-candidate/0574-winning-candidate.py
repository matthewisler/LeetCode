import pandas as pd

def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    vote_counter = vote.groupby('candidateId').size().reset_index(name='vote_count')
    winner_id = vote_counter.loc[vote_counter['vote_count'].idxmax(), 'candidateId']
    return candidate[candidate['id'] == winner_id][['name']]
