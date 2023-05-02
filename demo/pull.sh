#!/bin/bash

# 遍历当前文件夹中的所有子文件夹
for dir in */; do
    # 检查 .git 文件夹是否存在
    if [ -d "$dir/.git" ]; then
        echo "Executing git pull in $dir"
        # 进入子文件夹
        cd "$dir"
        # 执行 git pull
        git pull
        # 返回到上一级目录
        cd ..
        echo "Git pull completed in $dir"
    fi
done
