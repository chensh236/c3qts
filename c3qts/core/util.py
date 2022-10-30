import sys
import h5py
import os
from pathlib import Path
from typing import Dict, Tuple, Any
from packaging import version
import json
import pandas as pd

'''
获得平台的文件夹
'''
def _get_trader_dir(temp_name: str) -> Tuple[Path, Path]:
    """
    Get path where trader is running in.
    """
    cwd = Path.cwd()
    temp_path = cwd.joinpath(temp_name)

    # If .vntrader folder exists in current working directory,
    # then use it as trader running path.
    if temp_path.exists():
        return cwd, temp_path

    # Otherwise use home path of system.
    home_path = Path.home()
    temp_path = home_path.joinpath(temp_name)

    # Create .vntrader folder under home path if not exist.
    if not temp_path.exists():
        temp_path.mkdir()

    return home_path, temp_path

'''
获得文件夹的路径
'''
def get_file_path(filename: str) -> Path:
    """
    Get path for temp file with filename.
    """
    return TEMP_DIR.joinpath(filename)

TRADER_DIR, TEMP_DIR = _get_trader_dir(".tmp")

try:
    from loguru import logger
    # 1天1个log日志
    logger.add(os.path.join(TEMP_DIR, "sys.log"), rotation="1 day")
except Exception:
    class _logger:
        def info(self, *args, **kwargs):
            print(*args, file=sys.stderr, **kwargs)

        def error(self, *args, **kwargs):
            self.info(*args, **kwargs)

    logger = _logger()
    print("日志库loguru没有安装,日志文件输出功能不可用. 使用 pip install loguru 安装.",
          file=sys.stderr)

import yaml
if not os.path.exists(os.path.join(TEMP_DIR, "future_origin_data.yaml")):
    logger.error(f"应将期货原始数据的格式文件\"future_origin_data\"放置于目录 {TEMP_DIR}中")
    exit()
with open(os.path.join(TEMP_DIR, "future_origin_data.yaml"), "r", encoding="utf-8") as f:
    FUTURE_ORIGIN_CONF = yaml.safe_load(f)

class JsonHelper:
    def __init__(self) -> None:
        return
    
    @staticmethod
    def load_json(fp, mode):
        with open(fp, mode) as f:
            return json.load(f)
    
    @staticmethod
    def save_json(fp, mode, data):
        with open(fp, mode) as f:
            json.dump(data)

class H5Helper:
    def __init__(self, conf=None) -> None:
        self.conf = conf
        if conf is not None:
            if 'name' not in conf or 'field_name' not in conf or 'version' not in conf:
                logger.error(
                    f"日志配置必须包含'name' / 'field_name' / 'version' 等字段. 目前conf={conf}"
                )

    def save(self, filename, data, index=None):
        with h5py.File(name=filename, mode="w") as h5_file:
            if self.conf is not None:
                h5_file.create_dataset(name="ds", data=data, dtype=float)
                h5_file['ds'].attrs["field_name"] = self.conf["field_name"]
                h5_file['ds'].attrs["version"] = self.conf["version"]
                if index is not None:
                    h5_file.create_dataset(name="index", data=index, dtype=int)
            else:
                h5_file.create_dataset(name="ds", data=data, dtype=float)
                if index is not None:
                    h5_file.create_dataset(name="index", data=index, dtype=int)

    def load(self, filename, row_index = None, check: str = None):
        """
            filename: 文件地址
            row_index: 行索引. None 表示文件的所有行都会被读出来
            version_check: 
                none   :        不检查字段版本,加快运行时间
                'quick':        只检查field_name的长度
                'debug':        检查所有的字段名字以及版本号是否兼容
        """
        with h5py.File(filename, mode="r") as h5_file:
            data = h5_file['ds']
            index = None
            if 'index' in h5_file.keys():
                index = h5_file['index']
            if check is not None and self.conf is not None:
                check = check.lower()
                if 'field_name' not in data.attrs:
                    logger.error(
                        f"{filename} 的 attrs 没有字段信息. f{data.attrs.keys()}")
                    return None, None
                if check == "quick":
                    if len(data.attrs['field_name']) != len(
                            self.conf['field_name']):
                        logger.error(f"""{filename} 的字段数量与配置文件中指定的字段数量对不上. 
                            文件中: {len(data.attrs['field_name'])}.
                            配置中:{len(self.conf['field_name'])}""")
                        return None, None
                elif check == "debug":
                    if 'version' not in data.attrs:
                        logger.error(f"{filename} 没有 version 信息")
                        return None, None
                    if version.parse(data.attrs['version']) > version.parse(
                            self.conf['version']):
                        logger.error(
                            f"版本不兼容. {filename}版本为 {data.attrs['version']}. 配置文件中版本为{self.conf['version']}"
                        )
                        return None, None

            if row_index is None:
                return data[()], index
            else:
                return data[row_index][()], index

class CSVHelper:
    def __init__(self) -> None:
        return

    def save(self, filename, data):
        if type(data) != pd.core.frame.DataFrame:
            logger.error(f'{filename}:传入数据类型不为dataframe')
            return
        data.to_csv(filename)

    def load(self, filename, index_name=None):
        """
            filename: 文件地址
            index_name: 索引列，如果为None则使用默认的索引
            version_check: 
                none   :        不检查字段版本,加快运行时间
                'quick':        只检查field_name的长度
                'debug':        检查所有的字段名字以及版本号是否兼容
        """
        if not os.path.exists(filename):
            logger.error(f'{filename}:文件不存在')
        if index is None:
            return pd.read_csv(filename)
        else:
            return pd.read_csv(filename, index_col=index_name)


# future origin data h5 helper
fo_h5 = H5Helper(FUTURE_ORIGIN_CONF)
base_h5 = H5Helper()
csv_helper = CSVHelper()
RUNTYPE = "debug"