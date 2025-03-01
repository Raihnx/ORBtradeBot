import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timezone, timedelta

# Initialize MT5
if not mt5.initialize():
    print("❌ MT5 Initialization Failed!")
    quit()

SYMBOL = "EURUSD"  # Update if needed
TIMEFRAME = mt5.TIMEFRAME_M1  # 1-minute timeframe

now = datetime.now(timezone.utc)
start_time = now - timedelta(hours=1)  # Get data from last hour

# Fetch historical data
rates = mt5.copy_rates_range(SYMBOL, TIMEFRAME, start_time, now)

if rates is None or len(rates) == 0:
    print("❌ Failed to fetch data!")
else:
    df = pd.DataFrame(rates)
    print(df.tail())  # Print last few rows

mt5.shutdown()
