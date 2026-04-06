import pandas as pd

def load_data():
    sales = pd.read_csv("../data/m5-forecasting-accuracy/sales_train_validation.csv", nrows=1000)
    calendar = pd.read_csv("../data/m5-forecasting-accuracy/calendar.csv")
    prices = pd.read_csv("../data/m5-forecasting-accuracy/sell_prices.csv")
    return sales, calendar, prices

def clean_data(sales, calendar, prices):
    sales.fillna(0, inplace=True)
    calendar.fillna("None", inplace=True)
    prices.ffill(inplace=True)

    calendar['date'] = pd.to_datetime(calendar['date'])

    sales.drop_duplicates(inplace=True)
    calendar.drop_duplicates(inplace=True)
    prices.drop_duplicates(inplace=True)

    return sales, calendar, prices

def run_pipeline():
    sales, calendar, prices = load_data()
    sales, calendar, prices = clean_data(sales, calendar, prices)
    return sales, calendar, prices