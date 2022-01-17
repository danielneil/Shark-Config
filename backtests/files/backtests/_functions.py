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

def GenerateHTMLReport(strat, retAnalyzer, sharpeRatioAnalyzer, drawDownAnalyzer, tradesAnalyzer, plot, ticker):

    reportFileName = "/shark/reports/" + ticker + ".report.html"
    plotFileName = "/shark/reports/" + ticker + ".png"
    
    with open(reportFileName, 'w') as report_file:
        
        report_file.write("<html>")
        report_file.write("<head>")
        report_file.write("<title>Backtest Report - " + ticker + " </title>")
        report_file.write("</head>")
        report_file.write("<body>")                

        report_file.write("<h1>" + ticker + " - Backtest Report</h1>") 
        
        plt = plotter.StrategyPlotter(strat, True, False, True)
        plt.getInstrumentSubplot(instrument).addDataSeries("Entry SMA", strat.getEntrySMA())
        plt.getInstrumentSubplot(instrument).addDataSeries("Exit SMA", strat.getExitSMA())
        plt.savePlot(plotFileName)
        
        report_file.write("<img src=" + plotFileName + "/>")
        
        report_file.write("<table>")
        report_file.write("<tr>")
        
        report_file.write("<th>Final portfolio value</th>")
        report_file.write("<th>Cumulative returns</th>")
        
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

        report_file.write("<th>Sharpe ratio</th>")
        report_file.write("<th>Max. drawdown</th>")
        report_file.write("<th>Longest drawdown duration</th>")
        report_file.write("<th>Total trades</th>")
        report_file.write("<th>Wins</th>")
        report_file.write("<th>Losses</th>")

        report_file.write("</tr>")
        report_file.write("<tr>")
     
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
            
            report_file.write("<table>")
            report_file.write("<tr>")

            report_file.write("<th>LAvg. profit</th>")
            report_file.write("<th>LProfits std. dev.</th>")
            report_file.write("<th>LMax. profit</th>")
            report_file.write("<th>LMin. profit</th>")

            report_file.write("</tr>")
            report_file.write("<tr>")           
            
            report_file.write("<td>$%2.f</td>" % (profits.mean()))
            report_file.write("<td>$%2.f</td>" % (profits.std()))
            report_file.write("<td>$%2.f</td>" % (profits.max()))
            report_file.write("<td>$%2.f</td>" % (profits.min()))
        
            report_file.write("</tr>")
            report_file.write("</table>")
                      
            report_file.write("<br />")

            returns = tradesAnalyzer.getAllReturns()

            report_file.write("<table>")
            report_file.write("<tr>")
            
            report_file.write("<th>LAvg. return</th>")
            report_file.write("<th>LReturns std. dev.</th>")
            report_file.write("<th>LMax. return</th>")
            report_file.write("<th>LMin. return</th>")
            
            report_file.write("</tr>")
            report_file.write("<tr>")                 
            
            report_file.write("<td>%2.f</td>" % (returns.mean() * 100))
            report_file.write("<td>%2.f %%</td>" % (returns.std() * 100))
            report_file.write("<td>%2.f %%</td>" % (returns.max() * 100))
            report_file.write("<td>%2.f %%</td>" % (returns.min() * 100))
            
            report_file.write("</tr>")
            report_file.write("</table>") 

        if tradesAnalyzer.getProfitableCount() > 0:

            profits = tradesAnalyzer.getProfits()
            
            report_file.write("<table>")
            report_file.write("<tr>")

            report_file.write("<th>Avg. profit</th>")
            report_file.write("<th>Profits std. dev.</th>")
            report_file.write("<th>Max. profit</th>")
            report_file.write("<th>Min. profit</th>")

            report_file.write("</tr>")
            report_file.write("<tr>")           
            
            report_file.write("<td>$%2.f</td>" % (profits.mean()))
            report_file.write("<td>$%2.f</td>" % (profits.std()))
            report_file.write("<td>$%2.f</td>" % (profits.max()))
            report_file.write("<td>$%2.f</td>" % (profits.min()))
        
            report_file.write("</tr>")
            report_file.write("</table>")
                        
            report_file.write("<br />")

            returns = tradesAnalyzer.getPositiveReturns()
                       
            report_file.write("<table>")
            report_file.write("<tr>")

            report_file.write("<th>Avg. return</th>")
            report_file.write("<th>Returns std. dev.</th>")
            report_file.write("<th>Max. return</th>")
            report_file.write("<th>Min. return</th>")

            report_file.write("</tr>")
            report_file.write("<tr>")           
            
            report_file.write("<td>%2.f %%</td>" % (returns.mean() * 100))
            report_file.write("<td>%2.f %%</td>" % (returns.std() * 100))
            report_file.write("<td>%2.f %%</td>" % (returns.max() * 100))
            report_file.write("<td>%2.f %%</td>" % (returns.min() * 100))
        
            report_file.write("</tr>")
            report_file.write("</table>")
                                 
        if tradesAnalyzer.getUnprofitableCount() > 0:
            
            report_file.write("<br />")

            losses = tradesAnalyzer.getLosses()
                                    
            report_file.write("<table>")
            report_file.write("<tr>")

            report_file.write("<th>Avg. loss</th>")
            report_file.write("<th>Losses std. dev.</th>")
            report_file.write("<th>Max. loss</th>")
            report_file.write("<th>Min. loss</th>")

            report_file.write("</tr>")
            report_file.write("<tr>")           
            
            report_file.write("<td>$%2.f</td>" % (losses.mean()))
            report_file.write("<td>$%2.f</td>" % (losses.std()))
            report_file.write("<td>$%2.f</td>" % (losses.min()))
            report_file.write("<td>$%2.f</td>" % (losses.max()))
        
            report_file.write("</tr>")
            report_file.write("</table>")
                                              
            report_file.write("<br />")

            returns = tradesAnalyzer.getNegativeReturns()
  
            report_file.write("<table>")
            report_file.write("<tr>")

            report_file.write("<th>Avg. return</th>")
            report_file.write("<th>Returns std. dev.</th>")
            report_file.write("<th>Max. return</th>")
            report_file.write("<th>Min. return</th>")

            report_file.write("</tr>")
            report_file.write("<tr>")           
            
            report_file.write("<td> %2.f %%</td>" % (returns.mean() * 100))
            report_file.write("<td> %2.f %%</td>" % (returns.std() * 100))
            report_file.write("<td> %2.f %%</td>" % (returns.max() * 100))
            report_file.write("<td> %2.f %%</td>" % (returns.min() * 100))
        
            report_file.write("</tr>")
            report_file.write("</table>")
    
        report_file.write("</html>")
