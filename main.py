import time
from connect import connect_mt5
from trade_manager import execute_trades

def run_bot():
    """Runs the ORB15 bot and executes trades automatically"""
    if not connect_mt5():
        print("❌ Could not connect to MT5. Exiting...")
        return

    while True:
        now = datetime.now()
        if now.hour == 0 and now.minute == 15:  # Adjust based on market open time
            print("📌 Checking ORB15 setup...")
            execute_trades()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    run_bot()
