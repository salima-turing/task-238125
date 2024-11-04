import pytest
from behave import given, when, then, use_step_matcher

use_step_matcher("parse")

# Dummy data for testing
trade_data = [
    {"symbol": "AAPL", "quantity": 100, "price": 140.0},
    {"symbol": "MSFT", "quantity": 50, "price": 270.50},
]

account_balance = 10000.0


@given('the account balance is {balance:.2f}')
def step_impl(context, balance):
    global account_balance
    account_balance = float(balance)


@given('the following trades are available')
def step_impl(context):
    global trade_data
    trade_data = [dict(row.as_dict()) for row in context.table]


@when('I execute the trade for {symbol} with quantity {quantity} at price {price:.2f}')
def step_impl(context, symbol, quantity, price):
    for trade in trade_data:
        if trade["symbol"] == symbol:
            trade["quantity"] -= int(quantity)
            global account_balance
            account_balance += int(quantity) * float(price)
            break


@then('the account balance should be {balance:.2f}')
def step_impl(context, balance):
    assert account_balance == float(balance), f"Account balance should be {balance}, but it is {account_balance}"


@then('the trade quantity for {symbol} should be {quantity}')
def step_impl(context, symbol, quantity):
    for trade in trade_data:
        if trade["symbol"] == symbol:
            assert trade["quantity"] == int(
                quantity), f"Trade quantity for {symbol} should be {quantity}, but it is {trade['quantity']}"
            break


def test_trade_execution():
    """Test trade execution scenarios."""
    pass


if __name__ == "__main__":
    pytest.main()
