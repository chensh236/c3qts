'''
http://www.tinysoft.com.cn/tsdn/helpdoc/display.tsl?id=15446 郑商所数据问题
'''
import sys
sys.path.append('./../')
import os
from c3qts.core.util import JsonHelper
from c3qts.core.util import logger, fo_h5
from c3qts.core.settings import SETTINGS
from c3qts.core.merge import Merge
SETTINGS['database.basedir'] = '/14T/dev_database_factor/'
SETTINGS['tinysoft.username'] = 'sysbsquant'
SETTINGS['tinysoft.password'] = '123581'
SETTINGS['tinysoft.server_address'] = 'wh.tinysoft.com.cn'
SETTINGS['tinysoft.server_port'] = 443
# SETTINGS['tinysoft.username'] = 'gfzqjg'
# SETTINGS['tinysoft.password'] = 'gfquant@gf'

SETTINGS['email.hostname'] = 'smtp.qq.com'
SETTINGS['email.port'] = 465
SETTINGS['email.username'] = '1466196675@qq.com'
SETTINGS['email.password'] = 'achllzaepykxgdhj'
SETTINGS['email.forward'] = '1466196675@qq.com'

import ray
ray.init()

def worker(variety):
    
    '''
    如果是拼接因子数据，现版本需要手动输入因子名_窗口_作者，之后在上层叠加接口实现。
    如果factor_name为''则表示拼接行情数据。
    
    return True 正常拼接
    return False 拼接出错
    '''
    Merge.merge_zl_tick_data(variety=variety, factor_name='')
    '''
    如果是拼接因子数据，现版本需要手动输入因子名_窗口_作者，之后在上层叠加接口实现。
    如果factor_name为''则表示拼接行情数据；
    如果date_为空表示使用当天的数据，否则传入'YYYY-MM-DD'格式的日期。
    '''
    Merge.append_zl_tick_data(variety, date_='2023-03-11')
p_list = []
for variety in ['AG']:
    logger.info(f'主力合约合并 ##### {variety} #####')
    worker(variety)
    break
# ray.get(p_list)