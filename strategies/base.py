class StrategyBase:
    def __init__(self, df):
        self.df = df.copy()
        self.signals = []

    def generate_signals(self):
        raise NotImplementedError("Must override generate_signals()")

    def backtest(self):
        raise NotImplementedError("Must override backtest()")
