from strategies.base import StrategyBase

class SMACrossoverStrategy(StrategyBase):
    def __init__(self, df, short=9, long=20):
        super().__init__(df)
        self.short = short
        self.long = long

    def generate_signals(self):
        df = self.df
        df['sma_short'] = df['close'].rolling(self.short).mean()
        df['sma_long'] = df['close'].rolling(self.long).mean()
        df['position'] = (df['sma_short'] > df['sma_long']).astype(int)
        df['signal'] = df['position'].diff()
        self.df = df
        return df

    def backtest(self):
        trades = []
        position = None
        for idx, row in self.df.iterrows():
            if row['signal'] == 1:
                position = {'entry': idx, 'entry_price': row['close']}
            elif row['signal'] == -1 and position:
                trades.append({
                    'entry': position['entry'],
                    'exit': idx,
                    'pnl': row['close'] - position['entry_price']
                })
                position = None
        return trades
