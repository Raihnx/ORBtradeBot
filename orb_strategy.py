import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta

SYMBOL = "EURUSD"  # Change this to your trading pair

def get_orb_range():
    """Fetches market data and calculates the ORB15 range"""
    
    # Initialize MT5
    if not mt5.initialize():
        print("❌ MT5 Initialization Failed!")
        return None, None

    now = datetime.utcnow()  # MT5 uses UTC time
    start_time = now.replace(hour=20, minute=0, second=0, microsecond=0)  # Midnight UTC
    open_time = start_time + timedelta(minutes=15)  # First 15 minutes

    # Fetch historical data
    rates = mt5.copy_rates_range(SYMBOL, mt5.TIMEFRAME_M1, start_time, open_time)
    
    if rates is None or len(rates) == 0:
        print("❌ Failed to fetch market data")
        mt5.shutdown()
        return None, None

    df = pd.DataFrame(rates)
    high = df['high'].max()
    low = df['low'].min()

    # Shutdown MT5 after fetching data
    mt5.shutdown()
    
    return high, low

if __name__ == "__main__":
    high, low = get_orb_range()
    if high and low:
        print(f"📊 ORB15 High: {high}, ORB15 Low: {low}")
    else:
        print("⚠️ Could not retrieve ORB15 data.")
