import MetaTrader5 as mt5

# Initialize MT5
if not mt5.initialize():
    print("❌ MT5 Initialization Failed!")
    quit()

# Get available symbols
symbols = mt5.symbols_get()
symbol_names = [s.name for s in symbols]

# Check if EURUSD is in the list
if "EURUSD" in symbol_names:
    print("✅ EURUSD is available for trading!")
else:
    print("❌ EURUSD is NOT available. Check your broker!")

mt5.shutdown()
