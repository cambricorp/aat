from ...enums import OrderType, PairType, TickType
from ...structs import MarketData


class PoloniexMixins(object):
    def tickToData(self, jsn: dict) -> MarketData:
        raise NotImplementedError()

    def strToTradeType(self, s: str) -> TickType:
        raise NotImplementedError()

    def tradeReqToParams(self, req) -> dict:
        raise NotImplementedError()

    def currencyPairToString(self, cur: PairType) -> str:
        return cur.value[0].value + '_' + cur.value[1].value

    def orderTypeToString(self, typ: OrderType) -> str:
        raise NotImplementedError()


POLONIEX_CURRENCY_ID = {
    '1CR': '1',
    'ABY': '2',
    'AC': '3',
    'ACH': '4',
    'ADN': '5',
    'AEON': '6',
    'AERO': '7',
    'AIR': '8',
    'AMP': '275',
    'APH': '9',
    'ARCH': '258',
    'ARDR': '285',
    'ATOM': '313',
    'AUR': '10',
    'AXIS': '11',
    'BALLS': '12',
    'BANK': '13',
    'BAT': '302',
    'BBL': '14',
    'BBR': '15',
    'BCC': '16',
    'BCH': '292',
    'BCHABC': '308',
    'BCHSV': '309',
    'BCN': '17',
    'BCY': '269',
    'BDC': '18',
    'BDG': '19',
    'BELA': '20',
    'BITCNY': '273',
    'BITS': '21',
    'BITUSD': '272',
    'BLK': '22',
    'BLOCK': '23',
    'BLU': '24',
    'BNS': '25',
    'BNT': '305',
    'BONES': '26',
    'BOST': '27',
    'BTC': '28',
    'BTCD': '29',
    'BTCS': '30',
    'BTM': '31',
    'BTS': '32',
    'BURN': '33',
    'BURST': '34',
    'C2': '35',
    'CACH': '36',
    'CAI': '37',
    'CC': '38',
    'CCN': '39',
    'CGA': '40',
    'CHA': '41',
    'CINNI': '42',
    'CLAM': '43',
    'CNL': '44',
    'CNMT': '45',
    'CNOTE': '46',
    'COMM': '47',
    'CON': '48',
    'CORG': '49',
    'CRYPT': '50',
    'CURE': '51',
    'CVC': '294',
    'CYC': '52',
    'DAO': '279',
    'DASH': '60',
    'DCR': '277',
    'DGB': '53',
    'DICE': '54',
    'DIEM': '55',
    'DIME': '56',
    'DIS': '57',
    'DNS': '58',
    'DOGE': '59',
    'DRKC': '61',
    'DRM': '62',
    'DSH': '63',
    'DVK': '64',
    'EAC': '65',
    'EBT': '66',
    'ECC': '67',
    'EFL': '68',
    'EMC2': '69',
    'EMO': '70',
    'ENC': '71',
    'EOS': '298',
    'ETC': '283',
    'ETH': '267',
    'eTOK': '72',
    'EXE': '73',
    'EXP': '270',
    'FAC': '74',
    'FCN': '75',
    'FCT': '271',
    'FIBRE': '76',
    'FLAP': '77',
    'FLDC': '78',
    'FLO': '254',
    'FLT': '79',
    'FOAM': '307',
    'FOX': '80',
    'FRAC': '81',
    'FRK': '82',
    'FRQ': '83',
    'FVZ': '84',
    'FZ': '85',
    'FZN': '86',
    'GAME': '93',
    'GAP': '87',
    'GAS': '296',
    'GDN': '88',
    'GEMZ': '89',
    'GEO': '90',
    'GIAR': '91',
    'GLB': '92',
    'GML': '94',
    'GNO': '291',
    'GNS': '95',
    'GNT': '290',
    'GOLD': '96',
    'GPC': '97',
    'GPUC': '98',
    'GRC': '261',
    'GRCX': '99',
    'GRIN': '314',
    'GRS': '100',
    'GUE': '101',
    'H2O': '102',
    'HIRO': '103',
    'HOT': '104',
    'HUC': '105',
    'HUGE': '260',
    'HVC': '106',
    'HYP': '107',
    'HZ': '108',
    'IFC': '109',
    'INDEX': '265',
    'IOC': '263',
    'ITC': '110',
    'IXC': '111',
    'JLH': '112',
    'JPC': '113',
    'JUG': '114',
    'KDC': '115',
    'KEY': '116',
    'KNC': '301',
    'LBC': '280',
    'LC': '117',
    'LCL': '118',
    'LEAF': '119',
    'LGC': '120',
    'LOL': '121',
    'LOOM': '303',
    'LOVE': '122',
    'LPT': '312',
    'LQD': '123',
    'LSK': '278',
    'LTBC': '124',
    'LTC': '125',
    'LTCX': '126',
    'MAID': '127',
    'MANA': '306',
    'MAST': '128',
    'MAX': '129',
    'MCN': '130',
    'MEC': '131',
    'METH': '132',
    'MIL': '133',
    'MIN': '134',
    'MINT': '135',
    'MMC': '136',
    'MMNXT': '137',
    'MMXIV': '138',
    'MNTA': '139',
    'MON': '140',
    'MRC': '141',
    'MRS': '142',
    'MTS': '144',
    'MUN': '145',
    'MYR': '146',
    'MZC': '147',
    'N5X': '148',
    'NAS': '149',
    'NAUT': '150',
    'NAV': '151',
    'NBT': '152',
    'NEOS': '153',
    'NL': '154',
    'NMC': '155',
    'NMR': '310',
    'NOBL': '156',
    'NOTE': '157',
    'NOXT': '158',
    'NRS': '159',
    'NSR': '160',
    'NTX': '161',
    'NXC': '288',
    'NXT': '162',
    'NXTI': '163',
    'OMG': '295',
    'OMNI': '143',
    'OPAL': '164',
    'PAND': '165',
    'PASC': '289',
    'PAWN': '166',
    'PIGGY': '167',
    'PINK': '168',
    'PLX': '169',
    'PMC': '170',
    'POLY': '311',
    'POT': '171',
    'PPC': '172',
    'PRC': '173',
    'PRT': '174',
    'PTS': '175',
    'Q2C': '176',
    'QBK': '177',
    'QCN': '178',
    'QORA': '179',
    'QTL': '180',
    'QTUM': '304',
    'RADS': '274',
    'RBY': '181',
    'RDD': '182',
    'REP': '284',
    'RIC': '183',
    'RZR': '184',
    'SBD': '282',
    'SC': '268',
    'SDC': '185',
    'SHIBE': '186',
    'SHOPX': '187',
    'SILK': '188',
    'SJCX': '189',
    'SLR': '190',
    'SMC': '191',
    'SNT': '300',
    'SOC': '192',
    'SPA': '193',
    'SQL': '194',
    'SRCC': '195',
    'SRG': '196',
    'SSD': '197',
    'STEEM': '281',
    'STORJ': '297',
    'STR': '198',
    'STRAT': '287',
    'SUM': '199',
    'SUN': '200',
    'SWARM': '201',
    'SXC': '202',
    'SYNC': '203',
    'SYS': '204',
    'TAC': '205',
    'TOR': '206',
    'TRUST': '207',
    'TWE': '208',
    'UIS': '209',
    'ULTC': '210',
    'UNITY': '211',
    'URO': '212',
    'USDC': '299',
    'USDE': '213',
    'USDT': '214',
    'UTC': '215',
    'UTIL': '216',
    'UVC': '217',
    'VIA': '218',
    'VOOT': '219',
    'VOX': '276',
    'VRC': '220',
    'VTC': '221',
    'WC': '222',
    'WDC': '223',
    'WIKI': '224',
    'WOLF': '225',
    'X13': '226',
    'XAI': '227',
    'XAP': '228',
    'XBC': '229',
    'XC': '230',
    'XCH': '231',
    'XCN': '232',
    'XCP': '233',
    'XCR': '234',
    'XDN': '235',
    'XDP': '236',
    'XEM': '256',
    'XHC': '237',
    'XLB': '238',
    'XMG': '239',
    'XMR': '240',
    'XPB': '241',
    'XPM': '242',
    'XRP': '243',
    'XSI': '244',
    'XST': '245',
    'XSV': '246',
    'XUSD': '247',
    'XVC': '253',
    'XXC': '248',
    'YACC': '249',
    'YANG': '250',
    'YC': '251',
    'YIN': '252',
    'ZEC': '286',
    'ZRX': '293',
}


POLONIEX_PAIR_ID = {
    'BTC_ARDR': '177',
    'BTC_ATOM': '253',
    'BTC_BAT': '210',
    'BTC_BCH': '189',
    'BTC_BCHABC': '236',
    'BTC_BCHSV': '238',
    'BTC_BCN': '7',
    'BTC_BNT': '232',
    'BTC_BTS': '14',
    'BTC_BURST': '15',
    'BTC_CLAM': '20',
    'BTC_CVC': '194',
    'BTC_DASH': '24',
    'BTC_DCR': '162',
    'BTC_DGB': '25',
    'BTC_DOGE': '27',
    'BTC_EOS': '201',
    'BTC_ETC': '171',
    'BTC_ETH': '148',
    'BTC_FCT': '155',
    'BTC_FOAM': '246',
    'BTC_GAME': '38',
    'BTC_GAS': '198',
    'BTC_GNT': '185',
    'BTC_GRIN': '251',
    'BTC_HUC': '43',
    'BTC_KNC': '207',
    'BTC_LBC': '167',
    'BTC_LOOM': '213',
    'BTC_LPT': '250',
    'BTC_LSK': '163',
    'BTC_LTC': '50',
    'BTC_MAID': '51',
    'BTC_MANA': '229',
    'BTC_NAV': '61',
    'BTC_NMC': '64',
    'BTC_NMR': '248',
    'BTC_NXT': '69',
    'BTC_OMG': '196',
    'BTC_OMNI': '58',
    'BTC_PASC': '184',
    'BTC_POLY': '249',
    'BTC_PPC': '75',
    'BTC_QTUM': '221',
    'BTC_REP': '174',
    'BTC_SBD': '170',
    'BTC_SC': '150',
    'BTC_SNT': '204',
    'BTC_STEEM': '168',
    'BTC_STORJ': '200',
    'BTC_STR': '89',
    'BTC_STRAT': '182',
    'BTC_SYS': '92',
    'BTC_VIA': '97',
    'BTC_VTC': '100',
    'BTC_XCP': '108',
    'BTC_XEM': '112',
    'BTC_XMR': '114',
    'BTC_XPM': '116',
    'BTC_XRP': '117',
    'BTC_ZEC': '178',
    'BTC_ZRX': '192',
    'ETH_BAT': '211',
    'ETH_BCH': '190',
    'ETH_BNT': '233',
    'ETH_CVC': '195',
    'ETH_EOS': '202',
    'ETH_ETC': '172',
    'ETH_GAS': '199',
    'ETH_GNT': '186',
    'ETH_KNC': '208',
    'ETH_LOOM': '214',
    'ETH_LSK': '166',
    'ETH_MANA': '230',
    'ETH_OMG': '197',
    'ETH_QTUM': '222',
    'ETH_REP': '176',
    'ETH_SNT': '205',
    'ETH_STEEM': '169',
    'ETH_ZEC': '179',
    'ETH_ZRX': '193',
    'USDC_ATOM': '254',
    'USDC_BCH': '235',
    'USDC_BCHABC': '237',
    'USDC_BCHSV': '239',
    'USDC_BTC': '224',
    'USDC_DOGE': '243',
    'USDC_ETH': '225',
    'USDC_FOAM': '247',
    'USDC_GRIN': '252',
    'USDC_LTC': '244',
    'USDC_STR': '242',
    'USDC_USDT': '226',
    'USDC_XMR': '241',
    'USDC_XRP': '240',
    'USDC_ZEC': '245',
    'USDT_ATOM': '255',
    'USDT_BAT': '212',
    'USDT_BCH': '191',
    'USDT_BNT': '234',
    'USDT_BTC': '121',
    'USDT_DASH': '122',
    'USDT_DOGE': '216',
    'USDT_EOS': '203',
    'USDT_ETC': '173',
    'USDT_ETH': '149',
    'USDT_GNT': '217',
    'USDT_KNC': '209',
    'USDT_LOOM': '215',
    'USDT_LSK': '218',
    'USDT_LTC': '123',
    'USDT_MANA': '231',
    'USDT_NXT': '124',
    'USDT_QTUM': '223',
    'USDT_REP': '175',
    'USDT_SC': '219',
    'USDT_SNT': '206',
    'USDT_STR': '125',
    'USDT_XMR': '126',
    'USDT_XRP': '127',
    'USDT_ZEC': '180',
    'USDT_ZRX': '220',
    'XMR_BCN': '129',
    'XMR_DASH': '132',
    'XMR_LTC': '137',
    'XMR_MAID': '138',
    'XMR_NXT': '140',
    'XMR_ZEC': '181',
}
