import MetaTrader5 as mt5
from orb_strategy import get_orb_range

SYMBOL = "EURUSD"  # Trading pair

def place_order(symbol, order_type, price, sl, tp, lot_size=0.1):
    """Places a buy stop or sell stop order"""
    request = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": symbol,
        "volume": lot_size,
        "type": order_type,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": 1001,
        "comment": "ORB15 Bot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }
    
    result = mt5.order_send(request)
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        print(f"✅ Order placed: {order_type} at {price}")
    else:
        print(f"❌ Order failed: {result.comment}")

def execute_trades():
    """Executes trades based on ORB15 strategy"""
    high, low = get_orb_range()
    if high is None or low is None:
        return
    
    risk = (high - low) * 0.5  # Adjust risk
    sl_buy = high - risk
    tp_buy = high + (risk * 2)
    sl_sell = low + risk
    tp_sell = low - (risk * 2)

    # Place Buy Stop order above the ORB High
    place_order(SYMBOL, mt5.ORDER_TYPE_BUY_STOP, high + 0.0002, sl_buy, tp_buy)

    # Place Sell Stop order below the ORB Low
    place_order(SYMBOL, mt5.ORDER_TYPE_SELL_STOP, low - 0.0002, sl_sell, tp_sell)

if __name__ == "__main__":
    execute_trades()
