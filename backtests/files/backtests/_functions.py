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
        
        report_file.write("<html>")
        report_file.write("<head>")
        report_file.write("<title>Backtest Report - " + ticker + " </title>")
        report_file.write("</head>")
        report_file.write("<body>")                

        report_file.write("<h1>" + ticker + " - Backtest Report</h1>") 
        
        report_file.write("<table>")
        report_file.write("<tr>")
        
        report_file.write("<th>Final portfolio value:</th>")
        report_file.write("<th>Cumulative returns:</th>")
        
        report_file.write("</tr>")
        report_file.write("<tr>")
        
        report_file.write("<td>$%.2f</td>" % strat.getResult())
        report_file.write("<td>%.2f %%</td>" % (retAnalyzer.getCumulativeReturns()[-1] * 100))
        
        report_file.write("</tr>")
        report_file.write("</table>")
        
        report_file.write("<br />")
        
        sharpeRatio = sharpeRatioAnalyzer.getSharpeRatio(0.05)

        report_file.write("<table>")
        report_file.write("<tr>")

        report_file.write("<th>Sharpe ratio:</th>")
        report_file.write("<th>Max. drawdown:</th>")
        report_file.write("<th>Longest drawdown duration:</th>")
        report_file.write("<th>Total trades:</th>")
        report_file.write("<th>Wins:</th>")
        report_file.write("<th>Losses:</th>")

        report_file.write("</tr>")
        report_file.write("<tr>")
        
        report_file.write("Losses: %d" % (tradesAnalyzer.getUnprofitableCount()))

        report_file.write("<td>%.2f</td>" % (sharpeRatio))
        report_file.write("<td>%.2f %%</td>" % (drawDownAnalyzer.getMaxDrawDown() * 100))
        report_file.write("<td>%s</td>" % (drawDownAnalyzer.getLongestDrawDownDuration()))
        report_file.write("<td>%d</td>" % (tradesAnalyzer.getCount()))
        report_file.write("<td>%d</td>" % (tradesAnalyzer.getProfitableCount()))
        report_file.write("<td>%d</td>"  % (tradesAnalyzer.getUnprofitableCount()))
        
        report_file.write("</tr>")
        report_file.write("</table>")
        
        report_file.write("<br />")

        if tradesAnalyzer.getCount() > 0:

            profits = tradesAnalyzer.getAll()

            report_file.write("LAvg. profit: $%2.f</td></tr>" % (profits.mean()))
            report_file.write("LProfits std. dev.: $%2.f</td></tr>" % (profits.std()))
            report_file.write("LMax. profit: $%2.f</td></tr>" % (profits.max()))
            report_file.write("LMin. profit: $%2.f</td></tr>" % (profits.min()))
            
            report_file.write("<br />")

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
            
            report_file.write("<br />")

            returns = tradesAnalyzer.getPositiveReturns()

            report_file.write("Avg. return: %2.f %%" % (returns.mean() * 100))
            report_file.write("Returns std. dev.: %2.f %%" % (returns.std() * 100))
            report_file.write("Max. return: %2.f %%" % (returns.max() * 100))
            report_file.write("Min. return: %2.f %%" % (returns.min() * 100))

        if tradesAnalyzer.getUnprofitableCount() > 0:
            
            report_file.write("<br />")

            losses = tradesAnalyzer.getLosses()

            report_file.write("Avg. loss: $%2.f</td></tr>" % (losses.mean()))
            report_file.write("Losses std. dev.: $%2.f</td></tr>" % (losses.std()))
            report_file.write("Max. loss: $%2.f</td></tr>" % (losses.min()))
            report_file.write("Min. loss: $%2.f</td></tr>" % (losses.max()))
            
            report_file.write("<br />")

            returns = tradesAnalyzer.getNegativeReturns()

            report_file.write("Avg. return: %2.f %%" % (returns.mean() * 100))
            report_file.write("Returns std. dev.: %2.f %%" % (returns.std() * 100))
            report_file.write("Max. return: %2.f %%" % (returns.max() * 100))
            report_file.write("Min. return: %2.f %%" % (returns.min() * 100))
    
        report_file.write("</html>")
