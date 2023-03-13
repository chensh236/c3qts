# C3QTS系统的核心模块
<p align="center">
  <img src ="https://gitee.com/ccc-quantitative-team/img/raw/master/C3QTS%20%E4%B8%BBLOGO%20800x600.png"/>
</p>

<p align="center">
    <img src ="https://img.shields.io/badge/version-0.0.1-blueviolet.svg"/>
    <img src ="https://img.shields.io/badge/platform-windows|linux|macos-yellow.svg"/>
    <img src ="https://img.shields.io/badge/python-3.9-blue.svg" />
</p>

## 说明

量化交易系统核心模块，包括配置信息等
## 安装
1. virtualenv  venv(创建虚拟环境)
2. source venv/bin/activeate(激活虚拟环境)
3. pip3 install -r requirements.txt(pip安装modules)
4. 手动安装c3qts的相关组件。手动安装：进入文件夹里面，python3 setup.py install即可

## 使用

### Merge模块的使用
根据数据的特性，可将Merge模块分为主力合约数据、原始合约数据的拼合两个部分。

#### 主力合约数据的拼合
现有主力合约数据拼合有两个功能：
1. 拼合所有的主力合约数据（包括因子数据）：
```python
from c3qts_request.merge import Merge
# 拼合行情数据
Merge.merge_zl_tick_data(variety='AG')
# 拼合因子数据
Merge.merge_zl_tick_data(variety='AG', factor_name='active_trade_long_ratio_120_LRay')
```
需要注意的是，这里的主力合约判断方法沿用Tinysoft的判断方法，即使用成交量最大的合约作为次日主力合约。
2. 拼合特定日的主力合约数据（包括因子数据）:
```python
from c3qts_request.merge import Merge
Merge.append_zl_tick_data(variety='AG', date_='2023-03-11')
```
这里需要注意的是，如若传入日期`date_`早于已有数据的最晚日期，则取消拼合，显示错误：
```log
2023-03-13 16:16:28.228 | ERROR    | c3qts.core.merge:append_zl_tick_data:52 - 传入日期20230311早于或等于存储的最后日期20230311
```
#### 原始合约数据的拼合
现完成全部原始合约的数据拼合：
```python
Merge.merge_tick_data(variety='AG', sym='AG2301'):
```

## 版本更新
20221030 在h5读取/保存时添加索引列的数据
20230313 增加merge功能，合并主力数据
