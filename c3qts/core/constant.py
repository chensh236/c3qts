"""
General constant enums used in the trading platform.
"""

from enum import Enum

class DATATYPE(Enum):
    BASE_DATA = 'base_data'
    ZL_DATA = 'zl_data'
    RULE_DATA = 'rule_data'
    
class Direction(Enum):
    """
    Direction of order/trade/position.
    """
    LONG = "多"
    SHORT = "空"
    NET = "净"


class Offset(Enum):
    """
    Offset of order/trade.
    """
    NONE = ""
    OPEN = "开"
    CLOSE = "平"
    CLOSETODAY = "平今"
    CLOSEYESTERDAY = "平昨"


class Status(Enum):
    """
    Order status.
    """
    SUBMITTING = "提交中"
    NOTTRADED = "未成交"
    PARTTRADED = "部分成交"
    ALLTRADED = "全部成交"
    CANCELLED = "已撤销"
    REJECTED = "拒单"


class Product(Enum):
    """
    Product class.
    """
    EQUITY = "股票"
    FUTURES = "期货"
    OPTION = "期权"
    INDEX = "指数"
    FOREX = "外汇"
    SPOT = "现货"
    ETF = "ETF"
    BOND = "债券"
    WARRANT = "权证"
    SPREAD = "价差"
    FUND = "基金"
    EQUITY_FACTOR = "股票因子"
    FUTURES_FACTOR = "期货因子"
    OPTION_FACTOR = "期权因子"
    INDEX_FACTOR = "指数因子"
    FOREX_FACTOR = "外汇因子"
    SPOT_FACTOR = "现货因子"
    ETF_FACTOR = "ETF因子"
    BOND_FACTOR = "债券因子"
    WARRANT_FACTOR = "权证因子"
    SPREAD_FACTOR = "价差因子"
    FUND_FACTOR = "基金因子"


class OrderType(Enum):
    """
    Order type.
    """
    LIMIT = "限价"
    MARKET = "市价"
    STOP = "STOP"
    FAK = "FAK"
    FOK = "FOK"
    RFQ = "询价"


class OptionType(Enum):
    """
    Option type.
    """
    CALL = "看涨期权"
    PUT = "看跌期权"


class Exchange(Enum):
    """
    Exchange.
    """
    # Chinese
    # 这几个归为futures
    CFFEX = "CFFEX"         # China Financial Futures Exchange
    SHFE = "SHFE"           # Shanghai Futures Exchange
    CZCE = "CZCE"           # Zhengzhou Commodity Exchange
    DCE = "DCE"             # Dalian Commodity Exchange
    INE = "INE"             # Shanghai International Energy Exchange
    # 下面三个为stock
    SSE = "SSE"             # Shanghai Stock Exchange
    SZSE = "SZSE"           # Shenzhen Stock Exchange
    BSE = "BSE"             # Beijing Stock Exchange
    SGE = "SGE"             # Shanghai Gold Exchange
    WXE = "WXE"             # Wuxi Steel Exchange
    CFETS = "CFETS"         # CFETS Bond Market Maker Trading System
    XBOND = "XBOND"         # CFETS X-Bond Anonymous Trading System

    # Global
    SMART = "SMART"         # Smart Router for US stocks
    NYSE = "NYSE"           # New York Stock Exchnage
    NASDAQ = "NASDAQ"       # Nasdaq Exchange
    ARCA = "ARCA"           # ARCA Exchange
    EDGEA = "EDGEA"         # Direct Edge Exchange
    ISLAND = "ISLAND"       # Nasdaq Island ECN
    BATS = "BATS"           # Bats Global Markets
    IEX = "IEX"             # The Investors Exchange
    NYMEX = "NYMEX"         # New York Mercantile Exchange
    COMEX = "COMEX"         # COMEX of CME
    GLOBEX = "GLOBEX"       # Globex of CME
    IDEALPRO = "IDEALPRO"   # Forex ECN of Interactive Brokers
    CME = "CME"             # Chicago Mercantile Exchange
    ICE = "ICE"             # Intercontinental Exchange
    SEHK = "SEHK"           # Stock Exchange of Hong Kong
    HKFE = "HKFE"           # Hong Kong Futures Exchange
    SGX = "SGX"             # Singapore Global Exchange
    CBOT = "CBT"            # Chicago Board of Trade
    CBOE = "CBOE"           # Chicago Board Options Exchange
    CFE = "CFE"             # CBOE Futures Exchange
    DME = "DME"             # Dubai Mercantile Exchange
    EUREX = "EUX"           # Eurex Exchange
    APEX = "APEX"           # Asia Pacific Exchange
    LME = "LME"             # London Metal Exchange
    BMD = "BMD"             # Bursa Malaysia Derivatives
    TOCOM = "TOCOM"         # Tokyo Commodity Exchange
    EUNX = "EUNX"           # Euronext Exchange
    KRX = "KRX"             # Korean Exchange
    OTC = "OTC"             # OTC Product (Forex/CFD/Pink Sheet Equity)
    IBKRATS = "IBKRATS"     # Paper Trading Exchange of IB

    # Special Function
    LOCAL = "LOCAL"         # For local generated data


class Currency(Enum):
    """
    Currency.
    """
    USD = "USD"
    HKD = "HKD"
    CNY = "CNY"


class Interval(Enum):
    """
    Interval of bar data.
    """
    MINUTE = "1m"
    MIN_2 = "2m"
    MIN_3 = "3m"
    MIN_5 = "5m"
    MIN_10 = "10m"
    MIN_15 = "15m"
    MIN_20 = "20m"
    MIN_30 = "30m"
    HOUR = "1h"
    DAILY = "d"
    WEEKLY = "w"
    TICK = "tick"

class ContractType(Enum):
    '''
    Contract types
    '''
    # 原始合约
    ORI = 'ORIGIN'
    # 主力合约
    ZL = 'ZL'
    # 合约指数
    IDX = 'INDEX'
    # 连续合约
    LX = 'LX'
    # 连1
    LX1 = 'LX1'
    # 连2
    LX2 = 'LX2'
    # 连3
    LX3 = 'LX3'
    # 原始合约合并
    MERGE_ORI ='ORIGIN_MERGE'

"""
期货品种在天软中的主力合约映射
"""
class VarietyMap(Enum):
    '''
    品种和主力合约的映射
    原品种设为现品种的别名
    http://www.tinysoft.com.cn/TSDN/HelpDoc/display.tsl?id=12579
    '''
    AL = 'ZL000001'
    AU = 'ZL000002'
    CU = 'ZL000003'
    FU = 'ZL000004'
    RU = 'ZL000005'
    ZN = 'ZL000006'
    CF = 'ZL000007'
    OI = 'ZL000009'
    RO = 'ZL000009'
    SR = 'ZL000010'
    TA = 'ZL000011'
    WH = 'ZL000012'
    WS = 'ZL000012'
    PM = 'ZL000013'
    WT = 'ZL000013'
    A = 'ZL000014'
    B = 'ZL000015'
    C = 'ZL000016'
    L = 'ZL000017'
    M = 'ZL000018'
    P = 'ZL000019'
    Y = 'ZL000020'
    RI = 'ZL000021'
    ER = 'ZL000021'
    WR = 'ZL000022'
    RB = 'ZL000023'
    V = 'ZL000024'
    PB = 'ZL000025'
    J = 'ZL000026'
    MA = 'ZL000027'
    ME = 'ZL000027'
    AG = 'ZL000028'
    FG = 'ZL000029'
    RS = 'ZL000039'
    RM = 'ZL000031'
    JM = 'ZL000032'
    bU = 'ZL000033'
    I = 'ZL000034'
    ZC = 'ZL000035'
    TC = 'ZL000035'
    FB = 'ZL000036'
    BB = 'ZL000037'
    JR = 'ZL000038'
    JD = 'ZL000039'
    HC = 'ZL000040'
    PP = 'ZL000041'
    LR = 'ZL000042'
    SF = 'ZL000043'
    SM = 'ZL000044'
    CS = 'ZL000045'
    NI = 'ZL000046'
    SN = 'ZL000047'
    CY = 'ZL000048'
    AP = 'ZL000049'
    SC = 'ZL000050'
    SP = 'ZL000051'
    EG = 'ZL000052'
    CJ = 'ZL000053'
    NR = 'ZL000054'
    UR = 'ZL000055'
    RR = 'ZL000056'
    SS = 'ZL000057'
    EB = 'ZL000058'
    SA = 'ZL000059'
    PG = 'ZL000060'
    LU = 'ZL000061'
    PF = 'ZL000062'
    BC = 'ZL000063'
    LH = 'ZL000064'
    PK = 'ZL000065'

class ExchangeMap(Enum):
    """
    交易所和产品类型的映射
    """
    # 这几个归为futures
    CFFEX = Product.FUTURES # China Financial Futures Exchange
    SHFE = Product.FUTURES  # Shanghai Futures Exchange
    CZCE = Product.FUTURES  # Zhengzhou Commodity Exchange
    DCE = Product.FUTURES   # Dalian Commodity Exchange
    INE = Product.FUTURES   # Shanghai International Energy Exchange
    # 下面三个为stock
    SSE = Product.EQUITY    # Shanghai Stock Exchange
    SZSE = Product.EQUITY   # Shenzhen Stock Exchange
    BSE = Product.EQUITY    # Beijing Stock Exchange