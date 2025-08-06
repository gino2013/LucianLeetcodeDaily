#!/bin/bash

# 獲取當前日期，格式為 "yyyy-mm-dd"
current_date=$(date +"%Y-%m-%d")

# 定義來源資料夾和目標資料夾
source_folder="solutions/2025-03-12"  # 假設原始資料夾名稱為 2025-03-12
target_folder="solutions/${current_date}"

# 檢查來源資料夾是否存在
if [ -d "$source_folder" ]; then
    # 創建目標資料夾（如果不存在）
    mkdir -p "$target_folder"
    
    # 複製來源資料夾內容到目標資料夾
    cp -r "$source_folder"/* "$target_folder"/
    
    echo "成功將 ${source_folder} 複製到 ${target_folder}"
else
    echo "錯誤：來源資料夾 ${source_folder} 不存在"
    exit 1
fi
