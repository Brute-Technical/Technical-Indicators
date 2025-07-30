# utils/polygon_api.py

import requests
import pandas as pd
from config import POLYGON_API_KEY

def fetch_intraday(symbol, start, end, timespan='minute', limit=50000):
    url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/{timespan}/{start}/{end}"
    params = {
        "adjusted": "true",
        "sort": "asc",
        "limit": limit,
        "apiKey": POLYGON_API_KEY
    }
    r = requests.get(url, params=params).json()
    data = r.get("results", [])
    df = pd.DataFrame(data)
    if df.empty:
        return df
    df['t'] = pd.to_datetime(df['t'], unit='ms')
    df.set_index('t', inplace=True)
    df.rename(columns={'c': 'close'}, inplace=True)
    return df[['close']]
