# Shark-Config

This is the demo configuration for the Shark Automated Trading Platform.

Out of the box it comes with a sample configuration comprising of:

* [Main configuration](https://github.com/danielneil/Shark-Config/blob/master/trading-config.yml).
    * The sample demostrates using various Shark plugins against the CRYPTO TOP 20 (by Market Cap), namely: 
        * data - Downloads and imports yahoo finance historical data into Shark.
        * sma - Alerts to various simple moving average (sma) specifics.
        * strategy - Demostrates a simple moving averages cross over buy/sell strategy. 
        * backtest - Demostrates the use of a simple back test associated with the above.  
 
* [Sample Backtest code](https://github.com/danielneil/Shark-Config/blob/master/backtests/backtest_moving_averages.py) - Simple moving averages crossover.
* [Sample Strategy code](https://github.com/danielneil/Shark-Config/blob/master/strategies/moving_averages.py) - Buy/sell when a simple moving averages cross over occurs.

### Configuration resides in a git repo on the Shark server
```
# Check out the configuration for customisation.
git clone http://<shark_server>/Shark-Config.git
```
### Config Structure
```
trading-config.yml - Main configuration file, see sample.
backtests/ - Backtest code directory, see sample.
strategies/ - Strategy code directory, see sample.
bin/ - You have no power here (do not touch)
```
### Upon making a new configuration, commit it and then push back to the server as per regular git usage.
```
git add trading-config.yml backtests strategies
git commit -m 'DEMO Configuration, RSI2 backtest and strategy code'
git push
```
### Refresh the Shark server with your new configuration.
```
./bin/refresh.sh
```
### Main configuration file - trading-config.yml

The structure of the file is important (being yaml).


```yaml
---
- instrument: <instrument>
  group: <grouping of like instruments>
  plugin:
  - name: <name_of_plugin>
    desc: <description to appear on UI>
    group: <ui grouping of plugin>
    instrument: <instrument>
    <arg> : <arg
    <arg> : <arg>
    <arg> : <arg>
    <arg> : <arg
    ...
```

### Example - configuration for ticker BTC using several plugins (yahoo_finance_data, sma, backtest)

See the [plugins](https://github.com/danielneil/Shark/blob/main/doc/README.PLUGINS.md) for a list of capabilities.

```yaml
---
- instrument: BTC
  group: B
  plugin:
  - name: data
    provider: yahoo_finance
    desc: "Yahoo Finance [ Download of BTC Historical Data ]"
    group: "Yahoo Finance [ Historical Data ]"
    instrument: BTC
    start_date: 1597479263
    end_date: 1629015263
    interval: 1d
    adjusted_close: true
    frequency: daily
  - name: sma
    desc: "Simple Moving Average - 50 Days"
    group: "SMA: [ 50 Day ]"
    instrument: BTC
    period: 50
  - name: sma
    desc: "Simple Moving Average - 5 Days"
    group: "SMA: [ 5 Day ]"
    instrument: BTC
    period: 5
  - name: backtest
    desc: "BACKTEST: [ Moving Averages ]"
    group: "Backtesting"
    instrument: AMC
    file: backtest_moving_averages.py
    shares: 1000
    capital: 100000
```
