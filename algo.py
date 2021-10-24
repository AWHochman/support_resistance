import yfinance as yf
from datetime import datetime
import backtrader as bt
import backtrader.feeds as btfeeds
import backtrader.indicators as btind


class SupportResistence(bt.SignalStrategy):
    def notify_order(self, order):
        if order.status == bt.Order.Submitted or order.status == bt.Order.Accepted:
            return

        self.order_id = None

    def __init__(self):

    def next(self):

        if self.order_id:
            return

    def stop(self):
        print(f'Initial portfolio value: {self.broker.startingcash}')
        print(f'Final   portfolio value: {self.broker.getvalue()}')
        print(
            f'Return             rate: {self.broker.getvalue()/self.broker.startingcash}'
        )


def main():
    cerebro = bt.Cerebro()

    ma = bt.feeds.PandasData(
        dataname=yf.download('MA', datetime(2010, 1, 1), datetime(2011, 1, 1)))

    cerebro.adddata(ma)

    cerebro.addstrategy(SupportResistence)

    cerebro.run()
    # cerebro.plot()


if __name__ == '__main__':
    main()
