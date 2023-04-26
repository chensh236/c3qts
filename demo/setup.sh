#!/bin/bash

# 遍历当前文件夹中的所有子文件夹
for dir in */; do
    # 检查 setup.py 文件是否存在
    if [ -f "$dir/setup.py" ]; then
        echo "Installing library in $dir"
        # 使用 pip 安装库
        pip install -e "$dir"
    fi
done
