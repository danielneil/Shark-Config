# Shark-Default-Config

This is the main configuration repo for the Shark automated trading platform.

```yaml

# The structure of this file is important (as in indentation with it being yaml).
#
# <INSTRUMENT_NAME>:
#  INSTRUMENT_GROUP: "<NAME>"
#  <INDICATOR_GROUP>: "<NAME>"
#   DESCRIPTION: "<string that appears on the UI>"
#   COMMAND: <check_command>
#   <ARGUMENT>: <arg>
#   <ARGUMENT>: <arg>
#   <ARGUMENT>: <arg>
 
```

AMC:

 INSTRUMENT_GROUP: "Materials"
 
 RSI Check: 
  DESCRIPTION: "RSI [ 14 Day ]"
  COMMAND: check_rsi
  ticker: AMC
  period: 14
  min: 10
  max: 90

 Simple Moving Average - 50 Days:
  DESCRIPTION: "SMA: [ 50 Day ]"
  COMMAND: check_sma 
  ticker: AMC
  period: 50

 Simple Moving Average - 5 Days:
  DESCRIPTION: "SMA: [ 5 Day ]"
  check_command: check_sma
  ticker: AMC
  period: 5

 Opportunity Detection: 
  DESCRIPTION: "STRATEGY: [ Moving Averages ]"
  COMMAND: check_strategy
  ticker: AMC
  name: moving_averages.py
   
 Backtesting:
  DESCRIPTION: "BACKTEST: [ Moving Averages ]"
  COMMAND: check_backtest
  ticker: AMC
  name: backtest_moving_averages.py
  shares: 1000
  capital: 100000
