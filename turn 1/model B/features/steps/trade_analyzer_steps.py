# steps/trade_analyzer_steps.py

from behave import given, when, then
from trade_analyzer import TradeAnalyzer

@given('a list of trades')
def step_given_list_of_trades(context):
    context.trades = [
        {'symbol': 'AAPL', 'quantity': 100, 'price': 100, 'profit': 20},
        {'symbol': 'MSFT', 'quantity': 50, 'price': 200, 'profit': -50},
        {'symbol': 'GOOG', 'quantity': 200, 'price': 50, 'profit': 100}
    ]

@when('I calculate the profit and loss')
def step_when_calculate_profit_and_loss(context):
    context.trade_analyzer = TradeAnalyzer(context.trades)
    context.profit_loss = context.trade_analyzer.calculate_profit_loss()

@then('the total profit and loss should be calculated correctly')
def step_then_total_profit_and_loss_should_be_calculated_correctly(context):
    assert context.profit_loss == 50

@when('I count the winning trades')
def step_when_count_winning_trades(context):
    context.trade_analyzer = TradeAnalyzer(context.trades)
    context.winning_trades = context.trade_analyzer.count_winning_trades()

@then('the number of winning trades should be counted correctly')
def step_then_number_of_winning_trades_should_be_counted_correctly(context):

    assert context.winning_trades == 2
