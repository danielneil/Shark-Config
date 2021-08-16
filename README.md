# Shark-Config

### Configuration file for trading setup 

```
trading-config.yml
```

## Push configuration to local Shark server

```
 cd Shark-Config && ./push.sh
```

## Checkout configuration from local Shark server

```
 git clone http://<shark_server>/Shark-Config
```

### The structure of the file is important (being yaml).

```yaml
---
- instrument: <instrument>
  group: <grouping of like instruments>
  plugin:
  - name: <name_of_plugin>
    desc: <description to appear on UI>
    group: <ui grouping of plugin>
    instrument: AMC.AX
    start_date: 1597479263
    <arg> : <arg>
    <arg> : <arg>
    <arg> : <arg
    ...
```

### Example - configuration for ticker AMC using several plugins (rsi, sma, strategy, backtest)

See the [plugins](https://github.com/danielneil/Shark/blob/main/doc/README.PLUGINS.md) for a list of capabilities.

```yaml
---
- instrument: AMC
  group: Materials
  plugin:
  - name: yahoo_finance_data
    desc: "Yahoo Finance - Download of AMC Historical Data File"
    group: "Yahoo Finance - Historical Data"
    instrument: AMC.AX
    start_date: 1597479263
    end_date: 1629015263
    interval: 1d
    adjusted_close: true
    frequency: daily
  - name: rsi
    desc: RSI Check - 14 Days
    group: "RSI [ 14 Day ]"
    instrument: AMC
    period: 14
    min: 10
    max: 90
  - name: sma
    desc: "Simple Moving Average - 50 Days"
    group: "SMA: [ 50 Day ]"
    instrument: AMC
    period: 50
  - name: sma
    desc: "Simple Moving Average - 5 Days"
    group: "SMA: [ 5 Day ]"
    instrument: AMC
    period: 5
  - name: strategy
    desc: "STRATEGY - Moving Averages"
    group: "STRATEGY: [ Moving Averages ]"
    instrument: AMC
    file: moving_averages.py
  - name: backtest
    desc: "BACKTEST: [ Moving Averages ]"
    group: "Backtesting"
    instrument: AMC
    file: backtest_moving_averages.py
    shares: 1000
    capital: 100000
```
