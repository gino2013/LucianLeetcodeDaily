#!/usr/bin/env python3
"""
Smart LeetCode Daily Problem Setup Script
智能 LeetCode 每日問題設置腳本

Usage: 
  echo "problem content" | python3 daily_smart.py
  python3 daily_smart.py < problem.txt
  python3 daily_smart.py "problem content"
"""

import os
import sys
import subprocess
from datetime import datetime
from smart_parser import parse_problem


def run_command(command):
    """執行命令並返回結果"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"命令執行失敗: {command}")
        print(f"錯誤: {e.stderr}")
        return None


def get_today_folder():
    """獲取今天的資料夾路徑"""
    today = datetime.now().strftime("%Y-%m-%d")
    return f"solutions/{today}"


def create_daily_folder():
    """創建今日資料夾"""
    print("正在創建今日資料夾...")
    result = run_command("./tools/copy_folder.sh")
    if result is not None:
        print(f"✅ {result}")
        return True
    return False


def rename_files(folder_path, old_num, new_num):
    """重命名文件"""
    old_py = os.path.join(folder_path, f"{old_num}.py")
    old_md = os.path.join(folder_path, f"{old_num}.md")
    new_py = os.path.join(folder_path, f"{new_num}.py")
    new_md = os.path.join(folder_path, f"{new_num}.md")
    
    try:
        if os.path.exists(old_py):
            os.rename(old_py, new_py)
            print(f"✅ 重命名: {old_num}.py -> {new_num}.py")
        
        if os.path.exists(old_md):
            os.rename(old_md, new_md)
            print(f"✅ 重命名: {old_num}.md -> {new_num}.md")
        
        return new_py, new_md
    except Exception as e:
        print(f"❌ 重命名失敗: {e}")
        return None, None


def create_python_template(problem_info):
    """創建 Python 模板代碼"""
    return f"""from typing import List

class Solution:
    def solve(self, nums: List[int]) -> int:
        # TODO: Implement {problem_info['title_en']}
        # TODO: 實現 {problem_info['title_zh']}
        # Please modify method name and parameter types according to LeetCode requirements
        # 請根據 LeetCode 問題要求修改方法名和參數類型
        pass


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Add test cases here
    # 在此處添加測試案例
    pass
"""


def create_markdown_template(problem_info):
    """創建 Markdown 模板"""
    return f"""# {problem_info['number']}. {problem_info['title_en']}

## Problem Description

**Difficulty**: {problem_info['difficulty']}

{problem_info['description']}

## Solution Approach

### Method: [Algorithm Name]

<!-- Please describe the solution approach here -->

### Algorithm Steps:

1. <!-- Step 1 -->
2. <!-- Step 2 -->
3. <!-- Step 3 -->

## Code Implementation

```python
from typing import List

class Solution:
    def solve(self, nums: List[int]) -> int:
        # TODO: Implement {problem_info['title_en']}
        # Please modify method name and parameter types according to LeetCode requirements
        pass
```

## Complexity Analysis

- **Time Complexity**: O(?) <!-- Please fill in time complexity -->
- **Space Complexity**: O(?) <!-- Please fill in space complexity -->

## Example Tests

{problem_info['examples']}

## Key Points

1. <!-- Key point 1 -->
2. <!-- Key point 2 -->
3. <!-- Key point 3 -->

---

# {problem_info['number']}. {problem_info['title_zh']}

## 問題描述

**難度**: {problem_info['difficulty']}

{problem_info['description']}

## 解題思路

### 方法：[演算法名稱]

<!-- 請在此處描述解題思路 -->

### 算法步驟:

1. <!-- 步驟 1 -->
2. <!-- 步驟 2 -->
3. <!-- 步驟 3 -->

## 代碼實現

```python
from typing import List

class Solution:
    def solve(self, nums: List[int]) -> int:
        # TODO: 實現 {problem_info['title_zh']}
        # 請根據 LeetCode 問題要求修改方法名和參數類型
        pass
```

## 複雜度分析

- **時間複雜度**: O(?) <!-- 請填入時間複雜度 -->
- **空間複雜度**: O(?) <!-- 請填入空間複雜度 -->

## 範例測試

{problem_info['examples']}

## 關鍵要點

1. <!-- 關鍵點 1 -->
2. <!-- 關鍵點 2 -->
3. <!-- 關鍵點 3 -->
"""


def update_files(py_file, md_file, problem_info):
    """更新檔案內容"""
    try:
        # 更新 Python 檔案
        with open(py_file, 'w', encoding='utf-8') as f:
            f.write(create_python_template(problem_info))
        print(f"✅ 更新 Python 檔案: {py_file}")
        
        # 更新 Markdown 檔案
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(create_markdown_template(problem_info))
        print(f"✅ 更新 Markdown 檔案: {md_file}")
        
        return True
    except Exception as e:
        print(f"❌ 更新檔案失敗: {e}")
        return False


def main():
    print("🚀 Smart LeetCode Daily Problem Setup")
    print("=" * 40)
    
    # 讀取題目內容
    problem_text = ""
    
    if len(sys.argv) > 1:
        # 從命令行參數讀取
        problem_text = sys.argv[1]
        print("從命令行參數讀取題目內容")
    else:
        # 從標準輸入讀取或等待輸入
        print("請貼上題目內容，然後按 Ctrl+D 結束:")
        try:
            problem_text = sys.stdin.read()
            if problem_text:
                print("從標準輸入讀取題目內容")
        except KeyboardInterrupt:
            print("\n程序被取消")
            return
    
    if not problem_text.strip():
        print("❌ 沒有接收到題目內容")
        return
    
    # 解析題目信息
    print("\n📝 正在解析題目信息...")
    problem_info = parse_problem(problem_text)
    
    print(f"✅ 題目編號: {problem_info['number']}")
    print(f"✅ 英文標題: {problem_info['title_en']}")
    print(f"✅ 中文標題: {problem_info['title_zh']}")
    print(f"✅ 難度: {problem_info['difficulty']}")
    
    # 1. 創建今日資料夾
    if not create_daily_folder():
        print("❌ 無法創建今日資料夾，程序結束")
        return
    
    # 2. 確認資料夾路徑
    folder_path = get_today_folder()
    if not os.path.exists(folder_path):
        print(f"❌ 資料夾不存在: {folder_path}")
        return
    
    # 3. 找到舊檔案並重命名
    old_files = [f for f in os.listdir(folder_path) if f.endswith('.py')]
    if not old_files:
        print("❌ 找不到 Python 檔案")
        return
    
    old_num = old_files[0].replace('.py', '')
    py_file, md_file = rename_files(folder_path, old_num, problem_info['number'])
    
    if not py_file or not md_file:
        return
    
    # 4. 更新檔案內容
    if update_files(py_file, md_file, problem_info):
        print("\n🎉 設置完成!")
        print(f"📁 資料夾: {folder_path}")
        print(f"🐍 Python 檔案: {py_file}")
        print(f"📝 Markdown 檔案: {md_file}")
        print("\n💡 提示:")
        print("1. 請根據問題要求修改 Python 檔案中的方法名和參數")
        print("2. 請完善 Markdown 檔案中的解題思路")
    else:
        print("❌ 設置失敗")


if __name__ == "__main__":
    main()