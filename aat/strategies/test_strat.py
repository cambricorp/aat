from ..strategy import TradingStrategy
from ..structs import MarketData, TradeRequest, TradeResponse
from ..enums import Side, TradeResult, OrderType
from ..logging import STRAT as slog, ERROR as elog


class TestStrategy(TradingStrategy):
    def __init__(self) -> None:
        super(TestStrategy, self).__init__()
        self.active = False
        self.prev_state = ''
        self.state = ''

        self.bought = 0.0
        self.bought_qty = 0.0
        self.profits = 0.0

    def onBuy(self, res: TradeResponse) -> None:
        if res.status not in (TradeResult.FILLED, TradeResult.PARTIAL):
            slog.info('order failure: %s' % res)
            return

        if res.status == TradeResult.PARTIAL:
            slog.info('waiting to buy: %.2f @ %.2f' % (res.request.volume, res.request.price))

        else:
            self.active = True
            self.bought = res.volume*res.price
            self.bought_qty = res.volume
            slog.info('bought: %.2f @ %.2f for %.2f' % (res.volume, res.price, self.bought))

    def onSell(self, res: TradeResponse) -> None:
        if res.status not in (TradeResult.FILLED, TradeResult.PARTIAL):
            slog.info('order failure: %s' % res)
            return

        if res.status == TradeResult.PARTIAL:
            slog.info('waiting to sell: %.2f @ %.2f' % (res.request.volume, res.request.price))

        else:
            self.active = False
            sold = res.volume*res.price
            profit = sold - self.bought
            self.profits += profit
            slog.info('sold: %.2f @ %.2f for %.2f - %.2f - %.2f' % (res.volume, res.price, sold, profit, self.profits))
            self.bought = 0.0
            self.bought_qty = 0.0

    def onTrade(self, data: MarketData) -> bool:
        if not self.active:
            req = TradeRequest(side=Side.BUY,
                               volume=1.0,
                               instrument=data.instrument,
                               order_type=OrderType.MARKET,
                               exchange=data.exchange,
                               price=data.price)
            slog.info("requesting buy : %s", req)
            self.requestBuy(self.onBuy, req)
            self.active = True
            return True
        else:
            if self.bought_qty:
                req = TradeRequest(side=Side.SELL,
                                   volume=self.bought_qty,
                                   instrument=data.instrument,
                                   exchange=data.exchange,
                                   order_type=OrderType.MARKET,
                                   price=data.price)
                slog.info("requesting sell : %s", req)
                self.requestSell(self.onSell, req)
                self.active = False
                return True
            else:
                slog.info('None bought yet!')
        return False

    def onError(self, e) -> None:
        elog.critical(e, type(e))

    def onExit(self) -> None:
        self.cancelAll(lambda *args: True)

    def onChange(self, data: MarketData) -> None:
        pass

    def onFill(self, data: MarketData) -> None:
        pass

    def onCancel(self, data: MarketData) -> None:
        pass

    def onOpen(self, data: MarketData) -> None:
        pass

    def slippage(self, resp: TradeResponse) -> TradeResponse:
        return resp

    def transactionCost(self, resp: TradeResponse) -> TradeResponse:
        return resp

    def onAnalyze(self, portfolio_value, requests, responses) -> None:
        import pandas
        import matplotlib.pyplot as plt
        import seaborn as sns

        pd = pandas.DataFrame(portfolio_value, columns=['time', 'value'])
        pd.set_index(['time'], inplace=True)

        print(pd.iloc[1].value, pd.iloc[-1].value)

        sns.set_style('darkgrid')
        fig, ax1 = plt.subplots()

        plt.title('BTC algo 1 performance')
        ax1.plot(pd)

        ax1.set_ylabel('Portfolio value($)')
        ax1.set_xlabel('Date')
        for xy in [portfolio_value[0]] + [portfolio_value[-1]]:
            ax1.annotate('$%s' % xy[1], xy=xy, textcoords='data')
        plt.show()
