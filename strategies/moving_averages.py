#!/usr/bin/python

import pandas as pd
import datetime
import sys
import subprocess
import argparse

# Nagios constants. 

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = "Example strategy: Buy when the share price goes above 50 day simple moving average."

strategy_name = "Moving Averages - Cross Over"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker of the stock to run the strategy against.")
    parser.add_argument("-s", "--sma", help="Simple Moving Averages Period.")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    if not args.sma:
        print ("UNKNOWN - No sma specified")
        sys.exit(UNKNOWN)    
        
    ticker = args.ticker 
    sma_period = args.sma

    sma = Shark.Plugins.SMA(ticker, sma_period)
    price = Shark.Plugins.GetPrice(ticker)
    
    if price > sma:

       buy_str = "Buy Opportunity! - " + str(shorter_sma_periods) + " day SMA($" + str(short_sma).rstrip() + ") is above " + str(longer_sma_periods) + " day SMA ($" + str(long_sma).rstrip() + ")"
       print(buy_str)
       sys.exit(CRITICAL)

    print("No Opportunity")

    sys.exit(OK)
