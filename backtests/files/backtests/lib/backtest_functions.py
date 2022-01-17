    print("Final portfolio value: $%.2f" % strat.getResult())
    print("Cumulative returns: %.2f %%" % (retAnalyzer.getCumulativeReturns()[-1] * 100))

    sharpeRatio = sharpeRatioAnalyzer.getSharpeRatio(0.05)

    print("Sharpe ratio: %.2f" % (sharpeRatio))
    print("Max. drawdown: %.2f %%" % (drawDownAnalyzer.getMaxDrawDown() * 100))
    print("Longest drawdown duration: %s" % (drawDownAnalyzer.getLongestDrawDownDuration()))
    print("Total trades: %d" % (tradesAnalyzer.getCount()))
    print("Wins: %d" % (tradesAnalyzer.getProfitableCount()))
    print("Losses: %d" % (tradesAnalyzer.getUnprofitableCount()))

    if tradesAnalyzer.getCount() > 0:

        profits = tradesAnalyzer.getAll()

        print("LAvg. profit: $%2.f</td></tr>" % (profits.mean()))
        print("LProfits std. dev.: $%2.f</td></tr>" % (profits.std()))
        print("LMax. profit: $%2.f</td></tr>" % (profits.max()))
        print("LMin. profit: $%2.f</td></tr>" % (profits.min()))

        returns = tradesAnalyzer.getAllReturns()

        print("LAvg. return: %2.f %%" % (returns.mean() * 100))
        print("LReturns std. dev.: %2.f %%" % (returns.std() * 100))
        print("LMax. return: %2.f %%" % (returns.max() * 100))
        print("LMin. return: %2.f %%" % (returns.min() * 100))


    if tradesAnalyzer.getProfitableCount() > 0:

        profits = tradesAnalyzer.getProfits()

        print("Avg. profit: $%2.f" % (profits.mean()))
        print("Profits std. dev.: $%2.f" % (profits.std()))
        print("Max. profit: $%2.f" % (profits.max()))
        print("Min. profit: $%2.f" % (profits.min()))

        returns = tradesAnalyzer.getPositiveReturns()

        print("Avg. return: %2.f %%" % (returns.mean() * 100))
        print("Returns std. dev.: %2.f %%" % (returns.std() * 100))
       print("Max. return: %2.f %%" % (returns.max() * 100))
       print("Min. return: %2.f %%" % (returns.min() * 100))

    if tradesAnalyzer.getUnprofitableCount() > 0:

        losses = tradesAnalyzer.getLosses()

        print("Avg. loss: $%2.f</td></tr>" % (losses.mean()))
        print("Losses std. dev.: $%2.f</td></tr>" % (losses.std()))
        print("Max. loss: $%2.f</td></tr>" % (losses.min()))
        print("Min. loss: $%2.f</td></tr>" % (losses.max()))

        returns = tradesAnalyzer.getNegativeReturns()

        print("Avg. return: %2.f %%" % (returns.mean() * 100))
        print("Returns std. dev.: %2.f %%" % (returns.std() * 100))
        print("Max. return: %2.f %%" % (returns.max() * 100))
        print("Min. return: %2.f %%" % (returns.min() * 100))

