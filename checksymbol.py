import MetaTrader5 as mt5

# Initialize MT5
if not mt5.initialize():
    print("❌ MT5 Initialization Failed!")
    quit()

# Get available symbols
symbols = mt5.symbols_get()
symbol_names = [s.name for s in symbols]

# Print the first 20 symbols (to check availability)
print("Available symbols:", symbol_names[:20])

mt5.shutdown()
