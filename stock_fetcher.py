#!/usr/bin/env python
# coding: utf-8

# In[5]:


import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine


# In[7]:


from sqlalchemy import create_engine

try:
    engine = create_engine("mysql+pymysql://root:sahil%40123@localhost/live_stock")
    conn = engine.connect()
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print("❌ Error:", e)


# In[9]:


# fetching live data 
def fetch_and_store(ticker) :
    df = yf.download(ticker , period = "1y" , interval = "1d")
    df.reset_index(inplace = True)
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]
    df['ticker'] = ticker 

    #Save to SQL database
    df.to_sql('stock_data' , con = engine , if_exists = 'append' , index = False)
    print(f"✅Inserted {len(df)} rows for {ticker}")


# Run function Or Main function
if __name__ == "__main__":
    tickers = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS' , 'INFY.NS' , 'ICICIBANK.NS','KOTAKBANK.NS']
    for t in tickers:
        fetch_and_store(t)


# In[11]:


# ------------------ Get Latest Time from DB ------------------
def get_latest_time_from_db(ticker):
    query = f"""
        SELECT MAX(`Datetime`) as last_time 
        FROM stock_data 
        WHERE Ticker = '{ticker}'
    """
    result = pd.read_sql(query, con=engine)
    return result['last_time'].iloc[0] if not result.empty else None


# In[13]:


def fetch_and_store1(ticker):
    df = yf.download(ticker, period="1d", interval="1m", progress=False)

    if df.empty:
        print(f"⚠️ No data for {ticker}")
        return

    df.reset_index(inplace=True)
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    df['Ticker'] = ticker

    df['Datetime'] = pd.to_datetime(df['Datetime'], utc=True)

    latest_db_time = get_latest_time_from_db(ticker)
    if latest_db_time is not None:
        latest_db_time = pd.to_datetime(latest_db_time)
        if latest_db_time.tzinfo is None:
            latest_db_time = latest_db_time.tz_localize('UTC')
        df = df[df['Datetime'] > latest_db_time]
    print("🔎 Latest DB Time:", latest_db_time)
    if latest_db_time is not None:
        df = df[df['Datetime'] > pd.to_datetime(latest_db_time)]


    if not df.empty:
        df.to_sql('stock_data', con=engine, if_exists='append', index=False)
        print(f"✅ Inserted {len(df)} new rows for {ticker}")
    else:
        print(f"⏳ No new data for {ticker}")


# In[15]:


# ------------------ Market Hours Check ------------------
def is_market_open():
       now = datetime.now().time()
       open_time = datetime.strptime("09:15", "%H:%M").time()
       close_time = datetime.strptime("15:30", "%H:%M").time()
       return open_time <= now <= close_time


# In[17]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import schedule 
import time
from datetime import datetime


# In[ ]:


# ------------------ Scheduled Job ------------------
def job():
    if is_market_open():
        tickers = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS' , 'INFY.NS' , 'ICICIBANK.NS' , 'KOTAKBANK.NS']
        for t in tickers:
            fetch_and_store1(t)
    else:
        print("⏳ Market closed. Skipping data fetch...")

# ------------------ Start Scheduler ------------------
schedule.every(10).minutes.do(job)
print("✅ Scheduler started. Running every 10 minutes...")
job()

while True:
    schedule.run_pending()
    time.sleep(1)


# In[ ]:





# In[ ]:




