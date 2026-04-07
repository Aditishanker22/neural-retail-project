import pandas as pd

def create_long_format(sales):
    sales_long = sales.melt(
        id_vars=['id','item_id','dept_id','cat_id','store_id','state_id'],
        var_name='d',
        value_name='sales'
    )
    return sales_long

def merge_calendar(sales_long, calendar):
    df = sales_long.merge(calendar, on='d', how='left')
    return df

def merge_prices(df, prices):
    df = df.merge(prices, on=['store_id','item_id','wm_yr_wk'], how='left')
    return df

def create_time_features(df):
    df['date'] = pd.to_datetime(df['date'])

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['week'] = df['date'].dt.isocalendar().week
    df['weekday'] = df['date'].dt.weekday

    return df

def create_lag_features(df):
    df = df.sort_values(by=['id','date'])

    df['lag_7'] = df.groupby('id')['sales'].shift(7)
    df['lag_28'] = df.groupby('id')['sales'].shift(28)

    return df

def create_rolling_features(df):
    df['rolling_mean_7'] = df.groupby('id')['sales'].transform(lambda x: x.shift(7).rolling(7).mean())
    df['rolling_mean_28'] = df.groupby('id')['sales'].transform(lambda x: x.shift(28).rolling(28).mean())

    return df

def create_features(sales, calendar, prices):

    sales_long = create_long_format(sales)
    df = merge_calendar(sales_long, calendar)
    df = merge_prices(df, prices)

    df = create_time_features(df)
    df = create_lag_features(df)
    df = create_rolling_features(df)

    return df

