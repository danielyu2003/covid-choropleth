import pandas as pd

def _cases(state):
    '''
    Get the cumulative number of cases each day for a state as a dataframe.
    '''
    df = pd.read_csv("./data/us-states.csv")
    query_df = df[df['state'] == state][['date', 'state', 'cases']].reset_index(drop=True)
    query_df['date'] = pd.to_datetime(query_df['date'])
    sorted_df = query_df.sort_values(by=['date'])
    return sorted_df

def _difference(totals):
    '''
    Convert the array of cumulative cases to an array of the new cases each day.
    '''
    tmp = totals[0]
    for i in range(len(totals) - 1):
        diff = totals[i+1] - totals[i]
        totals[i] = tmp
        tmp = diff
    totals[-1] = tmp
    return totals

def preprocess(state):
    '''
    Convert the dataframe for the number of new cases each day into the format
    Prophet accepts, and get the maximum carrying capacity.
    '''
    df = _cases(state)
    df['cases'] = _difference(df['cases'].to_numpy())
    df = df.loc[df['cases'] >= 0]
    df.rename(columns={'date': "ds", 'cases': "y"}, inplace=True)
    df['floor'] = 0
    cap = max(df['y'])
    df['cap'] = cap
    return df, cap