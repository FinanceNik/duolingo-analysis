import pandas as pd
import datetime

months_string = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
current_year = datetime.datetime.now().year


def harmonize_data():
    df = pd.read_csv('./assets/leaderboards.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    df['year'] = df['timestamp'].dt.year
    df['month'] = df['timestamp'].dt.month
    return df


class Averages:
    def __init__(self):
        self.data = harmonize_data()

    def monthly(self):
        monthly_average = self.data.groupby('month')['score'].sum().mean()
        return "{:,.0f}".format(int(monthly_average))

    def yearly(self):
        yearly_average = self.data.groupby('year')['score'].sum().mean()
        return "{:,.0f}".format(int(yearly_average))

    def league(self):
        league_average = self.data['score'].mean()
        return "{:,.0f}".format(int(league_average))


class Totals:
    def __init__(self):
        self.data = harmonize_data()

    def total(self):
        total = self.data['score'].sum()
        return "{:,.0f}".format(int(total))


def yearly_score(year):
    data = harmonize_data()
    data = data.groupby('year')
    try:
        yearly = data.get_group(int(year))['score'].sum()

    except:
        yearly = 0.0

    return yearly


def monthly_score(year):
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

    return months_string, score


def cumulative_score_cumsum():
    data = harmonize_data()
    data = data.groupby('year')
    years = list(range(min(harmonize_data()['year']), max(harmonize_data()['year'])+1))
    months = list(range(1, 13))
    score = []
    for year in years:
        for month in months:
            try:
                monthly = data.get_group(int(year)).groupby('month').get_group(month)['score'].sum()
                score.append(monthly)
            except:
                monthly = 0.0
                score.append(monthly)

    return list(range(1, len(pd.Series(score).cumsum().tolist()))), pd.Series(score).cumsum().tolist()
