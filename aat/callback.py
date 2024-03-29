from abc import ABCMeta, abstractmethod
from .structs import MarketData
from .logging import LOG as log, DATA as dlog


class Callback(metaclass=ABCMeta):
    '''callback interface'''
    @abstractmethod
    def onTrade(self, data: MarketData):
        '''onTrade'''

    @abstractmethod
    def onOpen(self, data: MarketData):
        '''onOpen'''

    @abstractmethod
    def onFill(self, data: MarketData):
        '''onFill'''

    @abstractmethod
    def onCancel(self, data: MarketData):
        '''onCancel'''

    @abstractmethod
    def onChange(self, data: MarketData):
        '''onChange'''

    @abstractmethod
    def onError(self, data: MarketData):
        '''onError'''

    def onExit(self):
        '''onExit'''
        pass

    def onAnalyze(self, data):
        '''onAnalyze'''
        pass

    def onHalt(self, data):
        '''onHalt'''
        pass

    def onContinue(self, data):
        '''onContinue'''
        pass

    def callback(self):
        return self


class NullCallback(Callback):
    def __init__(self):
        pass

    def onTrade(self, data: MarketData) -> None:
        pass

    def onReceived(self, data: MarketData) -> None:
        pass

    def onOpen(self, data: MarketData) -> None:
        pass

    def onFill(self, data: MarketData) -> None:
        pass

    def onCancel(self, data: MarketData) -> None:
        pass

    def onChange(self, data: MarketData) -> None:
        pass

    def onError(self, data: MarketData) -> None:
        pass


class Print(Callback):
    def __init__(self,
                 onTrade=True,
                 onReceived=True,
                 onOpen=True,
                 onFill=True,
                 onCancel=True,
                 onChange=True,
                 onError=True):
        if not onTrade:
            setattr(self, 'onTrade', False)
        if not onReceived:
            setattr(self, 'onReceived', False)
        if not onOpen:
            setattr(self, 'onOpen', False)
        if not onFill:
            setattr(self, 'onFilled', False)
        if not onCancel:
            setattr(self, 'onCancelled', False)
        if not onChange:
            setattr(self, 'onChange', False)
        if not onError:
            setattr(self, 'onError', False)

    def onTrade(self, data: MarketData) -> None:
        dlog.info(str(data))

    def onReceived(self, data: MarketData) -> None:
        dlog.info(str(data))

    def onOpen(self, data: MarketData) -> None:
        dlog.info(str(data))

    def onFill(self, data: MarketData) -> None:
        dlog.info(str(data))

    def onCancel(self, data: MarketData) -> None:
        dlog.info(str(data))

    def onChange(self, data: MarketData) -> None:
        dlog.info(str(data))

    def onError(self, data: MarketData) -> None:
        dlog.info(str(data))

    def onAnalyze(self, data) -> None:
        log.info('Analysis')
        pass

    def onHalt(self, data) -> None:
        log.info('Halt')

    def onContinue(self, data) -> None:
        log.info('Continue')
