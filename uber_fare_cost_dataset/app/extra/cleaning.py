import pandas as pd


def clean_data(df):
    """Read the dataset and clean it."""

    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')

    df = df.dropna(subset=[
        'fare_amount',
        'pickup_longitude',
        'pickup_latitude',
        'dropoff_longitude',
        'dropoff_latitude']
    )

    df = df[df['fare_amount'] > 0]

    return df
