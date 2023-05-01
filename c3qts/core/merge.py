import os, stat, threading
from tqdm import tqdm
from c3qts.core.util import logger, fo_h5, base_h5, pkl_helper, RUNTYPE
from c3qts.core.constant import VarietyMap, ContractType
# from c3qts_request.broadcast import Broadcast
from datetime import date, datetime, timedelta
# from c3qts_request.request_util import get_variety
import numpy as np
from pathlib import Path
from c3qts.core.settings import SETTINGS
class Merge:
    _makedirs_lock = threading.Lock()
    @staticmethod
    # 追加最新的tick数据
    def append_zl_tick_data(database_dir: str, variety: str, date_:str ='', factor_name:str ='', author:str =''):
        # 修改因子名称为因子_作者名
        if len(factor_name) > 0 and len(author) == 0 or len(factor_name) == 0 and len(author) > 0:
            logger.error(f'因子{factor_name}, 作者{author}缺乏其中一个必要元素')
        factor_name = f'{factor_name}_{author}'
        # database_dir = database_dir
        # 如若date为空，则设置为当天日期
        if isinstance(date_, int):
            date_ = str(date_)
        if len(date_) == 0:
            today = date.today() - timedelta(days=1)
            date_ = today.strftime("%Y%m%d")
        else:
            try:
                _ = datetime.strptime(date_, "%Y%m%d")
            except ValueError:
                logger.error(f"日期{date_}的格式错误，应为YYYYMMDD")
                return False
        # 读取数据(后面更改为使用future_storage工具)
        input_fp = os.path.join(database_dir, '期货', 'tick', 'ORIGIN_MERGE', variety)
        output_fp = os.path.join(database_dir, '期货', 'tick', 'ZL', variety)
        if len(factor_name) > 1:
            input_fp = os.path.join(database_dir, '期货', '因子', factor_name, 'tick', 'ORIGIN_MERGE', variety)
            output_fp = os.path.join(database_dir, '期货', '因子', factor_name, 'tick', 'ZL', variety)
        zl_info_fp = os.path.join(database_dir, '期货', 'base_data', 'zl_data')
        curr_merge_data, curr_merge_index = None, None
        # 创建目录
        with Merge._makedirs_lock:
            if not os.path.exists(output_fp):
                os.makedirs(output_fp)
            else:
                if os.path.exists(os.path.join(output_fp, f'{variety}.h5')):
                    # 如若已存在文件则读取文件
                    curr_merge_data, curr_merge_index = fo_h5.load(os.path.join(output_fp, f'{variety}.h5'))
                else:
                    logger.info(f'{date_} - 品种{variety}不存在数据')
        dt_int = int(date_)
        # 判断传入日期的合法性
        if curr_merge_data is not None and curr_merge_data.shape[0] > 0:
            last_dt_int = int(curr_merge_data[-1, 0])
            if last_dt_int >= dt_int:
                logger.error(f'传入日期{dt_int}早于或等于存储的最后日期{last_dt_int}')
                return False 
        # 读取传入日期的主力合约信息
        # 这里的date是YYYYMMDD而不是YYYY-MM-DD，需要进行更改
        date_ = date_[:4] + '-' + date_[4:6] + '-' + date_[6:]
        try:
            df = pkl_helper.load(os.path.join(zl_info_fp, f'{date_}.h5'))
        except FileNotFoundError:
            logger.error(f'日期{date_}不存在主力合约信息，检查该日是否为交易日')
            return False
        df.index = df['主力代码']
        variety_code = eval(f'VarietyMap.{variety}.value')
        if variety_code not in df.index:
            logger.error(f'找不到{variety_code}对应的主力合约代码')
            return False
        sym = df.loc[variety_code, '合约代码']
        dt_int_start = int(f'{dt_int}000000000')
        dt_int_end = int(f'{dt_int}999999999')
        data, index = fo_h5.load(os.path.join(input_fp, f'{sym}.h5'), start=dt_int_start, end=dt_int_end)
        if data is not None:
            # 现存数据，判断传入的数据是否更新，如果更新则添加其中
            if data.shape[0] == 0:
                logger.error(f'{variety}在{date_}的数据为空')
                return False
            else:
                if curr_merge_data is None:
                    curr_merge_data = data
                else:
                    curr_merge_data = np.vstack([curr_merge_data, data])
                if curr_merge_index is None:
                    curr_merge_index = index
                else:
                    curr_merge_index = np.hstack([curr_merge_index, index])      
        if os.path.exists(os.path.join(output_fp, f'{variety}.h5')):
            os.remove(os.path.join(output_fp, f'{variety}.h5'))
        if curr_merge_data is None or curr_merge_data.shape[0] == 0:
            logger.error(f'品种{variety}的主力合约Tick数据为空')
            return False
        fo_h5.save(os.path.join(output_fp, f'{variety}.h5'), curr_merge_data, index=curr_merge_index)
        os.chmod(output_fp, stat.S_IRWXU | stat.S_IRWXG)
        # np.savetxt('测试.csv', curr_merge_data, delimiter=',')
        logger.info(f'{date_}: 品种{variety}的主力合约Tick数据合并成功')
        # Broadcast.log_content += f'品种{variety}的主力合约Tick数据合并成功\n'
        return True
    
    @staticmethod
    def sub_merge_zl_data(input_path: Path, last_sym: str, dt_int_start: int, dt_int_end: int, merge_data, merge_index):
        try:
            data, index = fo_h5.load(input_path / f'{last_sym}.h5', start=dt_int_start, end=dt_int_end)
        except FileNotFoundError as e:
            data, index = None, None
        if data is not None:
            if merge_data is None:
                merge_data = data
            else:
                merge_data = np.vstack([merge_data, data])
            if merge_index is None:
                merge_index = index
            else:
                merge_index = np.hstack([merge_index, index])
        return merge_data, merge_index
    
    '''
    根据因子名称以及作者名称获得不同周期的因子列表
    '''
    @staticmethod
    def get_factor_list(database_dir: str, variety: str, factor_name:str ='', author:str =''):
        if len(factor_name) == 0 and len(author) == 0:
            logger.error(f'因子{factor_name}, 作者{author}至少需要一个必要元素')
            return None
        database_dir = Path(database_dir)
        input_fp = database_dir / '期货' / '因子'
        file_list = os.listdir(input_fp)
        file_list.sort()
        file_list = [factor for factor in file_list if factor_name in factor or author in factor]
        return file_list
    
    # 合并主力tick数据
    '''
    2023-03-06
    更改原始的数据源为:MERGE_ORIGIN，取代原先的ORIGIN
    修正读取逻辑：
    如果不更新合约则只更新日期；如果更新合约则根据日期读取上一个合约
    '''
    @staticmethod
    def merge_zl_tick_data(database_dir: str, variety: str, factor_name:str ='', author:str =''):
        # 因子名称factor_name可以不包括名称，也可以包括名称
        if len(factor_name) == 0 and len(author) > 0:
            logger.error(f'如若数据为因子，因子名称{factor_name}必须存在')
            return False
        # 修改因子名称为因子_作者名
        database_dir = Path(database_dir)
        # 读取数据
        input_fp = database_dir / '期货' / 'tick' / 'ORIGIN_MERGE' / variety
        output_fp = database_dir / '期货' / 'tick' / 'ZL' / variety
        if len(factor_name) > 0:
            if len(author) > 0:
                factor_name = f'{factor_name}_{author}'
            input_fp = database_dir / '期货' / '因子' / factor_name / 'tick' / 'ORIGIN_MERGE' / variety
            output_fp = database_dir / '期货' / '因子' / factor_name / 'tick' / 'ZL' / variety
        zl_info_fp = database_dir / '期货' / 'base_data' / 'zl_data'
        
        # 创建目录
        with Merge._makedirs_lock:
            if not os.path.exists(output_fp):
                os.makedirs(output_fp)
        # 获取最早日期
        zl_info_date_list = os.listdir(zl_info_fp)
        zl_info_date_list.sort()
        merge_data = None
        merge_index = None
        # curr_sym的设置目的是防止向前看选择老的合约
        curr_sym = ''
        # 获取合约对应代码
        variety_code = eval(f'VarietyMap.{variety}.value')
        dt_int_start, dt_int_end = 0, 0
        refresh = False
        # 记录上个合约
        last_sym = ''
        
        # 是否仍为当前文件
        for idx, date_ in tqdm(enumerate(zl_info_date_list)):
            df = pkl_helper.load(os.path.join(zl_info_fp, date_))
            df.index = df['主力代码']
            if variety_code not in df.index:
                continue
            sym = df.loc[variety_code, '合约代码']
            # 确保主力合约的日期只能向前
            if curr_sym == '':
                curr_sym = sym
            if curr_sym < sym:
                refresh =True
                curr_sym = sym
            else:
                refresh = False
            
            dt_int = date_[:-3].replace('-', '')
            curr_dt_int_start = int(f'{dt_int}000000000')
            curr_dt_int_end = int(f'{dt_int}999999999')
            if dt_int_start == 0 or dt_int_end == 0:
                dt_int_start = curr_dt_int_start
                dt_int_end = curr_dt_int_end
            if not refresh:
                dt_int_end = curr_dt_int_end
                # 同一合约时跳过
                last_sym = curr_sym
            else:
                merge_data, merge_index = Merge.sub_merge_zl_data(input_fp, last_sym, dt_int_start, dt_int_end, merge_data, merge_index)
                dt_int_start = curr_dt_int_start
                dt_int_end = curr_dt_int_end         
                last_sym = curr_sym
            if idx == len(zl_info_date_list) - 1:
                merge_data, merge_index = Merge.sub_merge_zl_data(input_fp, last_sym, dt_int_start, dt_int_end, merge_data, merge_index)
        if os.path.exists(os.path.join(output_fp, f'{variety}.h5')):
            os.remove(os.path.join(output_fp, f'{variety}.h5'))
        if merge_data is None or merge_data.shape[0] == 0:
            logger.error(f'品种{variety}的主力合约Tick数据为空')
            return False
        fo_h5.save(os.path.join(output_fp, f'{variety}.h5'), merge_data, index=merge_index)
        os.chmod(output_fp, stat.S_IRWXU | stat.S_IRWXG)
        # np.savetxt('测试.csv', merge_data, delimiter=',')
        logger.info(f'品种{variety}的主力合约Tick数据合并成功')
        # Broadcast.log_content += f'品种{variety}的主力合约Tick数据合并成功\n'
        return True
    
    @staticmethod
    def merge_zl_daily_data(database_dir: str, variety):
        # TODO: 合并主力合约日频率数据
        return False
    
    @staticmethod
    def merge_tick_data(database_dir: str, variety: str, sym:str):
        # database_dir = database_dir
        # 读取数据
        input_fp = os.path.join(database_dir, '期货/tick/ORIGIN', variety, sym)
        output_fp = os.path.join(database_dir, '期货/tick/ORIGIN_MERGE', variety)
        if not os.path.exists(input_fp):
            logger.error(f'合约{sym}的Tick数据不存在, 路径:{input_fp}')
            # Broadcast.log_content += f'合约{sym}的Tick数据不存在\n'
            return False
        with Merge._makedirs_lock:
            if not os.path.exists(output_fp):
                os.makedirs(output_fp)
        file_list = os.listdir(input_fp)
        if len(file_list) == 0:
            logger.error(f'合约{sym}的Tick数据列表为空, 路径:{input_fp}')
            # Broadcast.log_content += f'合约{sym}的Tick数据不存在\n'
            return False
        file_list.sort()
        merge_data = None
        merge_index = None
        for filename in file_list:
            load_path = os.path.join(input_fp, filename)
            if not os.path.exists(load_path):
                logger.error(f'路径{load_path}不存在')
                continue
            data, index = fo_h5.load(load_path)
            if merge_data is None:
                merge_data = data
            else:
                merge_data = np.vstack([merge_data, data])
            if merge_index is None:
                merge_index = index
            else:
                merge_index = np.hstack([merge_index, index])
        if os.path.exists(os.path.join(output_fp, f'{sym}.h5')):
            os.remove(os.path.join(output_fp, f'{sym}.h5'))
        fo_h5.save(os.path.join(output_fp, f'{sym}.h5'), merge_data, index=merge_index)
        os.chmod(output_fp, stat.S_IRWXU | stat.S_IRWXG)
        logger.info(f'合约{sym}的Tick数据合并成功')
        # Broadcast.log_content += f'合约{sym}的Tick数据合并成功\n'
        return True