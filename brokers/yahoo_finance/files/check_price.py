#!/usr/bin/python3

import pandas as pd
import datetime
import numpy as np
import sys
import argparse
import os

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "This plugin checks the simple moving average (SMA) for a stock. Alerts Green (OK) if the share price is above the SMA, Yellow(Warning) if its below"

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock.")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    ticker = args.ticker
    
    history_dir = "/shark/historical/"yahoo_finance_data" + "/" + ticker + ".csv"
        
    try:
        f = open(datafile)
        f.close()
    except IOError:
        print("UNKNOWN - Waiting for historical data file - " + str(datafile))
        sys.exit(UNKNOWN)
        
    data = pd.read_csv(datafile)
    
    dataFrame = data['Adj Close']
    
    lastPrice = data['Adj Close'].iloc[-1]
    nextLastPrice = data['Adj Close'].iloc[-2]
       
    if lastPrice >  nextLastPrice:
        print("UP - Price $" + str(lastPrice) + " is above last price $" + str(nextLastPrice))
        sys.exit(OK)
            
    elif lastPrice <  nextLastPrice:
        print("DOWN - Price $" + str(lastPrice) + " is below last price $" + str(nextLastPrice))
        sys.exit(CRITICAL)      
