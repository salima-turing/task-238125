# features/trade_analyzer.feature

Feature: Trade Analyzer

  Scenario: Calculate Profit and Loss
    Given a list of trades
    When I calculate the profit and loss
    Then the total profit and loss should be calculated correctly

  Scenario: Count Winning Trades
    Given a list of trades
    When I count the winning trades
    Then the number of winning trades should be counted correctly
