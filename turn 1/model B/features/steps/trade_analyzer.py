# trade_analyzer.py

class TradeAnalyzer:
    def __init__(self, trades):
        self.trades = trades

    def calculate_profit_loss(self):
        profit_loss = 0
        for trade in self.trades:
            profit_loss += trade['profit']
        return profit_loss

    def count_winning_trades(self):
        winning_trades = [trade for trade in self.trades if trade['profit'] > 0]
        return len(winning_trades)
