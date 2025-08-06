# LeetCode Daily Setup 使用說明

## 概述

這個腳本自動化了每日 LeetCode 問題的設置流程，包括：
- 創建今日資料夾
- 重命名檔案為正確的問題編號
- 生成問題模板內容

## 使用方法

### 方法 1: 使用 daily 命令（推薦）

```bash
# 直接運行，會提示輸入問題資訊
./daily

# 或者提供 LeetCode URL（會嘗試解析問題 slug）
./daily "https://leetcode.com/problems/fruits-into-baskets-iii/description/?envType=daily-question&envId=2025-08-06"
```

### 方法 2: 直接運行 Python 腳本

```bash
# 直接運行
python3 leetcode_daily.py

# 或提供 URL
python3 leetcode_daily.py "https://leetcode.com/problems/problem-name/"
```

## 執行流程

1. **創建資料夾**: 自動調用 `copy_folder.sh` 創建今日資料夾
2. **輸入問題資訊**: 提示輸入以下資訊：
   - 問題編號（如：904, 3477）
   - 英文標題（如：Fruit Into Baskets）
   - 中文標題（如：水果成籃）
   - 難度（Easy/Medium/Hard）
3. **重命名檔案**: 將模板檔案重命名為正確的問題編號
4. **更新內容**: 用問題資訊更新 Python 和 Markdown 檔案的模板內容

## 範例執行

```bash
$ ./daily "https://leetcode.com/problems/fruits-into-baskets-iii/"

🚀 LeetCode Daily Problem Setup
========================================
輸入的 URL: https://leetcode.com/problems/fruits-into-baskets-iii/
正在創建今日資料夾...
✅ 成功將 solutions/2025-03-12 複製到 solutions/2025-08-06
從 URL 中檢測到問題: fruits-into-baskets-iii

請輸入以下問題資訊:
問題編號 (如 904, 3477): 904
英文標題 (如 'Fruit Into Baskets'): Fruit Into Baskets
中文標題 (如 '水果成籃'): 水果成籃
難度 (Easy/Medium/Hard): Medium

✅ 重命名: 2529.py -> 904.py
✅ 重命名: 2529.md -> 904.md
✅ 更新 Python 檔案: solutions/2025-08-06/904.py
✅ 更新 Markdown 檔案: solutions/2025-08-06/904.md

🎉 設置完成!
📁 資料夾: solutions/2025-08-06
🐍 Python 檔案: solutions/2025-08-06/904.py
📝 Markdown 檔案: solutions/2025-08-06/904.md

💡 提示:
1. 請根據問題要求修改 Python 檔案中的方法名和參數
2. 請完善 Markdown 檔案中的問題描述和解題思路
```

## 生成的檔案結構

執行完成後會在 `solutions/YYYY-MM-DD/` 資料夾中生成：

### Python 檔案 (`XXXX.py`)
```python
from typing import List

class Solution:
    def solve(self, nums: List[int]) -> int:
        # TODO: 實現 問題標題
        # 請根據問題要求修改方法名和參數
        pass
```

### Markdown 檔案 (`XXXX.md`)
包含完整的問題文檔模板：
- 問題描述區塊
- 解題思路區塊
- 代碼實現區塊
- 複雜度分析區塊
- 範例測試區塊
- 關鍵要點區塊

## 後續步驟

1. **修改 Python 檔案**：
   - 根據 LeetCode 問題要求修改方法名（如 `solve` -> `fruitsIntoBaskets`）
   - 修改參數類型和返回類型
   - 實現演算法邏輯

2. **完善 Markdown 檔案**：
   - 填入問題描述
   - 詳細說明解題思路
   - 分析時間和空間複雜度
   - 添加測試範例

## 故障排除

- **腳本無法執行**: 確保檔案有執行權限 `chmod +x daily`
- **資料夾已存在**: 腳本會跳過重複創建，直接重命名現有檔案
- **檔案不存在**: 檢查 `copy_folder.sh` 是否正確執行並創建了模板檔案