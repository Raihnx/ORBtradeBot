import MetaTrader5 as mt5

# Initialize MT5
if not mt5.initialize():
    print("❌ MT5 Initialization Failed!")
    quit()

SYMBOL = "EURUSD"  # Change if needed

# Check if the symbol is available
if mt5.symbol_select(SYMBOL, True):
    print(f"✅ {SYMBOL} is now enabled in Market Watch!")
else:
    print(f"❌ Failed to enable {SYMBOL}. Check your MT5!")

mt5.shutdown()
