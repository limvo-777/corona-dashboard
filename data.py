import pandas as pd

conditions=["confirmed","deaths","recovered"]

# read csv file0
daily_df = pd.read_csv("data/daily_report.csv")

# Total cases : 총 확진자
# filtering Columns, sum count, convert type series to dataframe
totals_df = daily_df[["Confirmed","Deaths","Recovered"]].sum().reset_index(name="count")
totals_df = totals_df.rename(columns={'index':"condition"})

# Group by Country name : 나라별 확진자
countries_df = daily_df[["Country_Region","Confirmed","Deaths","Recovered"]]
countries_df =countries_df.groupby("Country_Region").sum().sort_values(by="Confirmed",ascending=False).reset_index()

# parsing Country name in data
dropdown_options = countries_df.sort_values("Country_Region").reset_index()["Country_Region"]

# Daily Cases Globally : 일자별 확진자
# table of corona data sort by time
def make_global_df():
    def make_df(condition):
        df = pd.read_csv(f'data/time_{condition}.csv')
        # drop : ignore columns
        df = df.drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum().reset_index(name=condition)
        df = df.rename(columns={'index':'date'})
        return df
    final_df = None

    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df

# Daily Cases Country : 나라별 일일 확진자
# table of corona data sort by time
def make_country_df(country):
    def make_df(condition):
        df = pd.read_csv("data/time_confirmed.csv")
        df = df.loc[df["Country/Region"]==country]
        df = df.drop(columns=["Province/State","Country/Region","Lat","Long"]).sum().reset_index(name=condition)
        df = df .rename(columns={'index':'date'})
        return df
    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df
