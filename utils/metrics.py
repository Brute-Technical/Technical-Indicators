def evaluate(trades):
    if not trades: return {}
    total_pnl = sum(t['pnl'] for t in trades)
    win_rate = sum(1 for t in trades if t['pnl'] > 0) / len(trades)
    return {
        "Total PnL": round(total_pnl, 2),
        "Win Rate": round(win_rate * 100, 2),
        "Trades": len(trades)
    }
