# C3QTS系统的核心模块
<p align="center">
  <img src ="https://gitee.com/ccc-quantitative-team/img/raw/master/C3QTS%20%E4%B8%BBLOGO%20800x600.png"/>
</p>

<p align="center">
    <img src ="https://img.shields.io/badge/version-0.0.1-blueviolet.svg"/>
    <img src ="https://img.shields.io/badge/platform-windows|linux|macos-yellow.svg"/>
    <img src ="https://img.shields.io/badge/python-3.9-blue.svg" />
</p>

## C3QTS是什么？
c3qts（Customizable, Comprehensive, and Cutting-edge Quantitative Trading System）是一个综合性、可定制的量化交易系统，旨在为用户提供一个灵活、高效的交易策略研究和实现平台。该系统的设计背景是金融市场的复杂性和动态性，为了帮助用户更好地研究市场行为、因子选择和策略优化。

- Customizable（可定制）：系统具有高度的可定制性，用户可以根据需求定制因子、数据源和机器学习方法。
- Comprehensive（综合性）：系统涵盖了量化交易研究和实践所需的各种功能，使用户能够专注于策略本身，而无需过多关注底层细节。
- Cutting-edge（尖端）：系统采用最先进的技术和方法，为量化交易的进一步发展提供了强大的支持。

c3qts主要包含以下几个模块：
- c3qts_core：核心模块，包括constant.py、merge.py、settings.py和util.py，为整个系统提供基本的配置和工具函数。
- c3qts_factor：因子模块，包括factor_system和factor，实现因子计算和管理。
- c3qts_request：请求模块，包括request.py、request_util.py和broadcast.py，处理市场数据请求和广播。
- c3qts_datafeed：数据源模块，包括datafeed.py、tinysoft_datafeed.py、future_storage.py、localdb_database.py和storage_tool.py，实现数据的获取、处理和存储。
- c3qts_ml：机器学习模块，包括asset_data.py和basemodel.py，用于处理金融数据并应用机器学习方法进行建模和预测。
- c3qts_backtest: 回测模块。
c3qts的目的是为量化交易研究和实践提供一个一站式解决方案。通过整合因子计算、数据源管理、请求处理和机器学习方法，该系统可以帮助用户更方便地开发、测试和优化交易策略。

系统的特点包括：
- 高度模块化：各模块之间相互独立，便于开发和维护。
- 可定制性：用户可以根据需要定制因子、数据源和机器学习方法。
- 易用性：通过封装和抽象，提供了简洁易用的API接口。
- 扩展性：系统设计灵活，可以方便地增加新的因子、数据源和机器学习模型。

c3qts是一个包括了多个Python模块的高频期货投研系统（后期扩展接入交易模块），其中每个模块都有自己的特定功能。`c3qts_localdb`模块用于读取基本数据、行情数据以及因子数据（支持bar级别数据的读取以及tick级别的读取）；`c3qts_datafeed`模块提供了从数据源（如Tinysoft）读取数据和管理数据的功能。`c3qts_request`模块则提供了向数据提供商请求数据的功能；`c3qts_factor`模块是用于生成和处理因子的抽象类。其他因子继承自该类以实现多态；`c3qts_ml`模块是机器学习模块，用于生成机器学习算法所需的训练数据、验证数据和测试数据。该模块的主要类是AssetData，它可以读取标的资产的历史数据并生成相应的训练数据、验证数据和测试数据。另外还有BaseModel和DeepModel以支持传统机器学习方法以及深度学习方法；`c3qts_backtesting`模块是用于回测交易策略的模块，它提供了回测框架、回测结果统计等功能。最重要的核心模块是`c3qts`模块，它提供了多个功能模块所需的共同支持。例如，它定义了高频期货投研系统（后期扩展接入交易模块）中使用的常量和工具函数，并提供了数据合并和设置管理功能。

这些模块共同构成了`c3qts`仓库，可以提供一个完整的高频期货投研系统（后期扩展接入交易模块）解决方案，包括数据管理、因子生成、机器学习和交易策略回测等方面。`c3qts`的优势在于其集成了量化交易研究和实践所需的各种功能，使用户能够专注于策略本身，而无需过多关注底层细节。此外，其高度模块化的设计使得系统易于扩展和维护，为量化交易的进一步发展提供了强大的支持。

## 说明

c3qts是一个强大的量化交易系统，它的核心模块包括`constant.py`、`merge.py`、`settings.py`和`util.py`。作为最重要的核心模块，它为其他模块提供了基础设施和实用功能，实现了多个子模块之间的协同工作。

`constant.py`模块定义了系统中通用的一些常量，如交易所、合约类型、数据周期等，为其他模块提供了统一的参考标准。`merge.py`模块提供了用于合并不同数据源和时间周期的数据的功能，以满足用户对于多周期和多种数据类型的需求。settings.py模块负责系统设置的管理，使用户可以方便地配置和自定义系统的行为。`util.py`模块提供了一系列实用工具函数，如日志记录、时间处理和数据处理等，为其他模块提供了高效的实用功能。

c3qts核心模块在系统中发挥着关键作用，确保了整个系统的稳定性和可扩展性。其他模块依赖于核心模块来实现具体的功能，从而使得整个系统协同高效地运行。

## 安装

1. virtualenv  venv(创建虚拟环境)
2. source venv/bin/activeate(激活虚拟环境)
3. pip3 install -r requirements.txt(pip安装modules，仅第一次需要执行)
4. 手动安装c3qts的相关组件。手动安装：进入文件夹里面，python3 setup.py install即可
5. 将`conf/future_origin_data.yaml`复制到`home`目录的`.tmp`文件夹中

## 函数解析
```
core/constant.py
core/merge.py
core/settings.py
core/util.py
```
### constant

- DATATYPE：用于表示不同类型的数据，如基础数据、主力合约数据和规则数据。
- Direction：用于表示订单/交易/仓位的方向，包括多头（LONG）、空头（SHORT）和净仓位（NET）。
- Offset：表示订单/交易的开平仓方式，包括无、开仓（OPEN）、平仓（CLOSE）、平今（CLOSETODAY）和平昨（CLOSEYESTERDAY）。
- Status：用于表示订单状态，包括提交中（SUBMITTING）、未成交（NOTTRADED）、部分成交（PARTTRADED）、全部成交（ALLTRADED）、已撤销（CANCELLED）和拒单（REJECTED）。
- Product：表示产品类型，包括股票、期货、期权、指数、外汇、现货、ETF、债券、权证、价差和基金等。
- OrderType：表示订单类型，包括限价（LIMIT）、市价（MARKET）、止损（STOP）、FAK、FOK和询价（RFQ）。
- OptionType：表示期权类型，包括看涨期权（CALL）和看跌期权（PUT）。
- Exchange：表示交易所类型，包括中国和全球的各大交易所，如上海证券交易所（SSE）、纽约证券交易所（NYSE）等。
- Currency：表示货币类型，包括美元（USD）、港元（HKD）和人民币（CNY）。
- Interval：表示K线图的时间间隔，包括1分钟、2分钟、3分钟、5分钟、10分钟、15分钟、20分钟、30分钟、1小时、日线、周线和TICK数据。
- ContractType：表示合约类型，包括原始合约、主力合约、合约指数、连续合约和原始合约合并等。
- VarietyMap：表示期货品种与天软中的主力合约映射关系。
- ExchangeMap：表示交易所与产品类型的映射关系。

### merge
根据数据的特性，可将Merge模块分为主力合约数据、原始合约数据的拼合两个部分。
#### append_zl_tick_data

```python
append_zl_tick_data(database_dir: str, variety: str, date_: str = '', factor_name: str = '', author: str = '')
```
功能：追加最新的主力合约Tick数据。

参数：

variety (str)：品种，例如：'AG'。
date_ (str)：日期，默认为空，此时为前一天的日期；如若不为空，则格式为：'YYYYMMDD'。注意：date_需要时精确的日期。
factor_name (str)：因子名称，默认为空。
author (str)：作者名，默认为空。
使用方法：

```python
Merge.append_zl_tick_data(database_dir: str, variety='AG', date_='20230101', factor_name='Factor1', author='Author1')
```
这里需要注意的是，如若传入日期`date_`早于已有数据的最晚日期，则取消拼合，显示错误：
```log
2023-03-13 16:16:28.228 | ERROR    | c3qts.core.merge:append_zl_tick_data:52  传入日期20230311早于或等于存储的最后日期20230311
```

#### append_zl_tick_data

```python
from c3qts.core.merge import Merge
sub_merge_zl_data(input_path: Path, last_sym: str, dt_int_start: int, dt_int_end: int, merge_data, merge_index)
```

功能：合并主力合约数据的子函数。

参数：

input_path (Path)：输入路径，数据文件的路径。
last_sym (str)：上一个合约符号。
dt_int_start (int)：开始日期时间整数。
dt_int_end (int)：结束日期时间整数。
merge_data：合并后的数据。
merge_index：合并后的索引。
使用方法：
通常不需要直接调用此方法，它将在 merge_zl_tick_data 方法中被调用。

#### merge_zl_tick_data

```python
merge_zl_tick_data(database_dir: str, variety: str, factor_name: str = '', author: str = '')
```

功能：合并主力合约Tick数据。

参数：

variety (str)：品种，例如：'IF'。
factor_name (str)：因子名称，默认为空。
author (str)：作者名，默认为空。
使用方法：

```python
from c3qts.core.merge import Merge
Merge.merge_zl_tick_data(database_dir, variety='IF', factor_name='Factor1', author='Author1')
```

#### merge_zl_daily_data (未完成)

```python
merge_zl_daily_data(database_dir: str, variety)
```

功能：合并主力合约日频率数据。

参数：

variety (str)：品种，例如：'AG'。
使用方法：

```python
Merge.merge_zl_daily_data(database_dir, variety='AG')
```
注意：此方法尚未实现，返回 False。

#### merge_tick_data

```python
merge_tick_data(database_dir: str, variety: str, sym: str)
```

功能：该函数用于拼合原始的主力合约（只针对于`ContractType.ORI`），场景是每日的定时获取

参数：

variety (str)：品种，例如：'AG'。
sym (str)：合约符号，例如：'AG2101'。
使用方法：

```python
Merge.merge_tick_data(database_dir, variety='AG', sym='AG2101')
```

### settings
settings首先导入了一些必要的库，如json和typing。然后定义了save_json和load_json两个函数，它们分别用于将数据保存到临时文件夹中的JSON文件以及从JSON文件中加载数据。在这段代码中，还定义了一个全局设置字典SETTINGS，用于存储全局配置信息。

函数说明：

save_json(filename: str, data: dict) -> None：
此函数将数据data保存为临时文件夹中的JSON文件。参数filename表示JSON文件的名称。此函数无返回值。

load_json(filename: str) -> dict：
此函数从临时文件夹中的JSON文件加载数据。参数filename表示JSON文件的名称。此函数返回一个字典，包含从JSON文件中加载的数据。

get_settings(prefix: str = "") -> Dict[str, Any]：
此函数根据指定的前缀prefix从全局设置字典SETTINGS中获取设置信息。返回一个字典，包含与指定前缀匹配的设置信息。

在代码的末尾，还使用load_json函数从名为st_settings.json的文件中加载全局设置，并将其添加到SETTINGS字典中。

使用方法：
通常只是将settings引入到环境中：
```python
from c3qts.core.settings import SETTINGS
```
此时c3qts读取得到的参数是默认的参数，即：
```json
SETTINGS: Dict[str, Any] = {
    "database.database": "future_seq_data",
    "database.name": "localdb",
}
```
之后可以使用SETTINGS这个字典来编辑参数，如：
```python
SETTINGS['database.basedir'] = '/14T/dev_database_factor'
```

如果有参数的读取和保存需求：
```python
from c3qts.core.settings import *
```
此时c3qts会从`~/.tmp/st_settings.json`中读取参数。如果需要保存，需语句：
```python
save_json(SETTING_FILENAME, SETTINGS)
```
即可完成参数的保存，路径在：`~/.tmp/st_settings.json`

### util

功能：工具类。通常从util中引入`fo_h5`以及`base_h5`，分别用于保存行情数据以及基本信息；引入`logger`输出日志。

常用三个变量：fo_h5, base_h5, pkl_helper以及实例`logger`的定义如下：
```python
from loguru import logger
fo_h5 = H5Helper(FUTURE_ORIGIN_CONF)
base_h5 = H5Helper()
pkl_helper = PKLHelper()
```

使用方法：
```python
from c3qts.core.util import logger, fo_h5, base_h5, pkl_helper
```

#### 主力合约数据的拼合
现有主力合约数据拼合有两个功能：
1. 拼合所有的主力合约数据（包括因子数据）：
```python
from c3qts.core.merge import Merge
# 拼合行情数据
Merge.merge_zl_tick_data(database_dir, variety='AG')
# 拼合因子数据
Merge.merge_zl_tick_data(database_dir, variety='AG', factor_name='active_trade_long_ratio_120', author='LRay')
```
需要注意的是，这里的主力合约判断方法沿用Tinysoft的判断方法，即使用成交量最大的合约作为次日主力合约。

2. 拼合特定日的主力合约数据（包括因子数据）:
```python
from c3qts.core.merge import Merge
# 合并行情数据
Merge.append_zl_tick_data(database_dir: str, variety='AG', date_='20230311')
# 拼合因子数据
Merge.append_zl_tick_data(database_dir: str, variety='AG', date_='20230311', factor_name='active_trade_long_ratio_120', author='LRay')
```

#### 原始合约数据的拼合
现完成全部原始合约的数据拼合：
```python
Merge.merge_tick_data(database_dir, variety='AG', sym='AG2301'):
```

## 版本更新
20221030 在h5读取/保存时添加索引列的数据
20230313 增加merge功能，合并主力数据
20230315 修改merge_zl_tick_data的接口，factor_name改为factor_name加author
