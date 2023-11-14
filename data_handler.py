import pandas as pd
import matplotlib.pyplot as plt

months_string = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def harmonize_data():
    df = pd.read_csv('./assets/leaderboards.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    df['year'] = df['timestamp'].dt.year
    df['month'] = df['timestamp'].dt.month
    df['day'] = df['timestamp'].dt.day

    return df


def yearly_score(year):
    data = harmonize_data()
    data = data.groupby('year')
    try:
        yearly = data.get_group(int(year))['score'].sum()

    except:
        yearly = 0.0

    return yearly


def monthly_score(year, month):
    data = harmonize_data()
    data = data.groupby('year')
    months = list(range(1, 13))
    score = []
    for month in months:
        try:
            monthly = data.get_group(int(year)).groupby('month').get_group(month)['score'].sum()
            score.append(monthly)
        except:
            monthly = 0.0
            score.append(monthly)

    return score, months_string

