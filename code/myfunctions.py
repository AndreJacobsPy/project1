import pandas as pd
import datetime as dt

def convert_date(df: pd.DataFrame, date_col: str):
    '''
    Doc: This function takes a column from a dataframe
    and changes the different parts of the datetime into
    seperate columns

    arguments:
    df: any dataframe that contains the datetime column
    in question

    date_col: the string that corresponds to the column
    name. this is used for subsetting the dataframe.

    returns: None, but the initial dataframe is changed 
    in the function
    '''
    # converting the column containing date to a datetime object
    df[date_col] = pd.to_datetime(df[date_col])

    df['month'] = df[date_col].dt.month
    df['weekday'] = df[date_col].dt.weekday
    df['day'] = df[date_col].dt.day
    df['hour'] = df[date_col].dt.hour
    df['minute'] = df[date_col].dt.minute