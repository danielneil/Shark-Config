#!/usr/bin/python3.9

from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed

from pyalgotrade.technical import ma
from pyalgotrade.technical import cross

from pyalgotrade.stratanalyzer import sharpe
from pyalgotrade.stratanalyzer import drawdown
from pyalgotrade.stratanalyzer import trades
from pyalgotrade import plotter
import pyalgotrade
from pyalgotrade import plotter

import argparse
import sys
import os

import time

import pandas as pd
import json

def GenerateJSONReport(strat, retAnalyzer, sharpeRatioAnalyzer, drawDownAnalyzer, tradesAnalyzer, plot, ticker):

    plotFileName = "/shark/reports/" + ticker + ".png"
    plot.savePlot(plotFileName)
    
    jsonBacktestSummary = "/shark/reports/" + ticker + ".backtest.summary.json"          
    with open(jsonBacktestSummary, 'w', encoding='utf-8') as f:

        sharpeRatio = sharpeRatioAnalyzer.getSharpeRatio(0.05)

        json_obj = {}
        json_obj['backtest_summary'] = []

        json_obj['backtest_summary'].append({
            'ticker': ticker,
            'final_portfolio_value': strat.getResult(),
            'cumulative_returns': (retAnalyzer.getCumulativeReturns()[-1] * 100),
            'sharpe_ratio': sharpeRatio,
            'max_drawdown': (drawDownAnalyzer.getMaxDrawDown() * 100),
            'longest_drawdown_duration': str(drawDownAnalyzer.getLongestDrawDownDuration()),
            'total_trades': str(tradesAnalyzer.getCount()), 
            'wins': str(tradesAnalyzer.getProfitableCount()),
            'losses': str(tradesAnalyzer.getUnprofitableCount())
            })

        json.dump(json_obj, f)

    jsonBacktestTotalTrades = "/shark/reports/" + ticker + ".backtest.totaltrades.json"
    with open(jsonBacktestTotalTrades, 'w', encoding='utf-8') as f:

        if tradesAnalyzer.getCount() > 0:

            profits = tradesAnalyzer.getAll()          
            returns = tradesAnalyzer.getAllReturns()

            json_obj = {}
            json_obj['total_trades'] = []

            json_obj['total_trades'].append({
                'avg_profit': profits.mean(),
                'profits_std_dev': profits.std(),
                'max_profit': profits.max(),
                'min_profit': profits.min(),
                'avg_return': (returns.mean() * 100),
                'returns_std_dev': (returns.std() * 100),
                'max_return': (returns.max() * 100),
                'min_return': (returns.min() * 100)
                })

            json.dump(json_obj, f)

    jsonBacktestProfitableTrades = "/shark/reports/" + ticker + ".backtest.profitabletrades.json"
    with open(jsonBacktestProfitableTrades, 'w', encoding='utf-8') as f:

        if tradesAnalyzer.getProfitableCount() > 0:

            profits = tradesAnalyzer.getProfits()
            returns = tradesAnalyzer.getPositiveReturns()

            json_obj = {}
            json_obj['profitable_trades'] = []

            json_obj['profitable_trades'].append({
                'avg_profit':  profits.mean(),
                'profits_std_dev': profits.std(), 
                'max_profit': profits.max(),
                'min_profit': profits.min(),
                'avg_return': (returns.mean() * 100),
                'returns_std_dev': (returns.std() * 100),
                'max_return': (returns.max() * 100),
                'min_return': (returns.min() * 100)
                })

            json.dump(json_obj, f)

    jsonBacktestUnprofitableTrades = "/shark/reports/" + ticker + ".backtest.unprofitabletrades.json"
    with open(jsonBacktestUnprofitableTrades, 'w', encoding='utf-8') as f:

        if tradesAnalyzer.getUnprofitableCount() > 0:
            
            losses = tradesAnalyzer.getLosses()
            returns = tradesAnalyzer.getNegativeReturns()

            json_obj = {}
            json_obj['unprofitable_trades'] = []

            json_obj['unprofitable_trades'].append({
                'avg_loss': losses.mean(),
                'losses_std_dev': losses.std(),
                'max_loss': losses.min(),
                'min_loss': losses.max(),
                'avg_return': (returns.mean() * 100),
                'returns_std_dev': (returns.std() * 100),
                'max_return': (returns.max() * 100),
                'min_return': (returns.min() * 100)
                })

            json.dump(json_obj, f)

