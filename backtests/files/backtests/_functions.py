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

import argparse
import sys
import os

import time

import pandas as pd

def GenerateHTMLReport(strat, retAnalyzer, sharpeRatioAnalyzer, drawDownAnalyzer, tradesAnalyzer, plot, ticker):

    reportFileName = "/shark/reports/" + ticker + ".report.html"

    with open(reportFileName, 'w') as report_file:

        report_file.write("Final portfolio value: $%.2f" % strat.getResult())
        report_file.write("Cumulative returns: %.2f %%" % (retAnalyzer.getCumulativeReturns()[-1] * 100))

        sharpeRatio = sharpeRatioAnalyzer.getSharpeRatio(0.05)

        report_file.write("Sharpe ratio: %.2f" % (sharpeRatio))
        report_file.write("Max. drawdown: %.2f %%" % (drawDownAnalyzer.getMaxDrawDown() * 100))
        report_file.write("Longest drawdown duration: %s" % (drawDownAnalyzer.getLongestDrawDownDuration()))
        report_file.write("Total trades: %d" % (tradesAnalyzer.getCount()))
        report_file.write("Wins: %d" % (tradesAnalyzer.getProfitableCount()))
        report_file.write("Losses: %d" % (tradesAnalyzer.getUnprofitableCount()))

        if tradesAnalyzer.getCount() > 0:

            profits = tradesAnalyzer.getAll()

            report_file.write("LAvg. profit: $%2.f</td></tr>" % (profits.mean()))
            report_file.write("LProfits std. dev.: $%2.f</td></tr>" % (profits.std()))
            report_file.write("LMax. profit: $%2.f</td></tr>" % (profits.max()))
            report_file.write("LMin. profit: $%2.f</td></tr>" % (profits.min()))

            returns = tradesAnalyzer.getAllReturns()

            report_file.write("LAvg. return: %2.f %%" % (returns.mean() * 100))
            report_file.write("LReturns std. dev.: %2.f %%" % (returns.std() * 100))
            report_file.write("LMax. return: %2.f %%" % (returns.max() * 100))
            report_file.write("LMin. return: %2.f %%" % (returns.min() * 100))


        if tradesAnalyzer.getProfitableCount() > 0:

            profits = tradesAnalyzer.getProfits()

            report_file.write("Avg. profit: $%2.f" % (profits.mean()))
            report_file.write("Profits std. dev.: $%2.f" % (profits.std()))
            report_file.write("Max. profit: $%2.f" % (profits.max()))
            report_file.write("Min. profit: $%2.f" % (profits.min()))

            returns = tradesAnalyzer.getPositiveReturns()

            report_file.write("Avg. return: %2.f %%" % (returns.mean() * 100))
            report_file.write("Returns std. dev.: %2.f %%" % (returns.std() * 100))
            report_file.write("Max. return: %2.f %%" % (returns.max() * 100))
            report_file.write("Min. return: %2.f %%" % (returns.min() * 100))

        if tradesAnalyzer.getUnprofitableCount() > 0:

            losses = tradesAnalyzer.getLosses()

            report_file.write("Avg. loss: $%2.f</td></tr>" % (losses.mean()))
            report_file.write("Losses std. dev.: $%2.f</td></tr>" % (losses.std()))
            report_file.write("Max. loss: $%2.f</td></tr>" % (losses.min()))
            report_file.write("Min. loss: $%2.f</td></tr>" % (losses.max()))

            returns = tradesAnalyzer.getNegativeReturns()

            report_file.write("Avg. return: %2.f %%" % (returns.mean() * 100))
            report_file.write("Returns std. dev.: %2.f %%" % (returns.std() * 100))
            report_file.write("Max. return: %2.f %%" % (returns.max() * 100))
            report_file.write("Min. return: %2.f %%" % (returns.min() * 100))

