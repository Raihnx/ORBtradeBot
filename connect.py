import MetaTrader5 as mt5

# Replace with your Exness MT5 account details (DO NOT SHARE PUBLICLY)
ACCOUNT_NUMBER = 104101291
PASSWORD = "Ireems@123"  # Change your password immediately for security!
SERVER = "Exness-MT5Real15"  # Check your broker's server

# Update the correct MT5 installation path
MT5_PATH = MT5_PATH = "C:\\Program Files\\MetaTrader 5 EXNESS\\terminal64.exe"
  # Adjust this path

def connect_mt5():
    print("📌 Initializing MT5...")

    if not mt5.initialize(path=MT5_PATH):
        print("❌ MT5 Initialization Failed!", mt5.last_error())
        return False

    if not mt5.login(ACCOUNT_NUMBER, PASSWORD, SERVER):
        print("❌ Login Failed!", mt5.last_error())
        return False

    print("✅ Successfully Connected to MT5!")
    return True

connect_mt5()
