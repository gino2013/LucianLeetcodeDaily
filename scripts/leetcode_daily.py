#!/usr/bin/env python3
"""
LeetCode Daily Problem Setup Script
自動化處理每日 LeetCode 問題的腳本

Usage: python3 leetcode_daily.py [leetcode_url]
"""

import os
import sys
import subprocess
import re
from datetime import datetime


def run_command(command):
    """執行命令並返回結果"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"命令執行失敗: {command}")
        print(f"錯誤: {e.stderr}")
        return None


def extract_problem_slug_from_url(url):
    """從 LeetCode URL 中提取問題 slug"""
    pattern = r'leetcode\.com/problems/([^/\?]+)'
    match = re.search(pattern, url)
    return match.group(1) if match else None


def default_example_text():
    """返回預設範例文字"""
    return '''**Example 1:**
```
Input: 
Output: 
Explanation: 
```

**範例 1:**
```
輸入: 
輸出: 
解釋: 
```'''


def default_description_text():
    """返回預設問題描述文字"""
    return '<!-- Please add problem description here -->\n\n<!-- 請在此處添加問題描述 -->'


def extract_examples_from_description(description):
    """從問題描述中提取範例"""
    examples = []
    example_pattern = r'Example\s+(\d+):\s*\n(.*?)(?=Example\s+\d+:|$)'
    matches = re.findall(example_pattern, description, re.DOTALL | re.IGNORECASE)
    
    if matches:
        example_text = ""
        for i, (num, content) in enumerate(matches):
            example_text += f"**Example {num}:**\n```\n{content.strip()}\n```\n\n"
            example_text += f"**範例 {num}:**\n```\n{content.strip()}\n```\n\n"
        return example_text.strip()
    
    return default_example_text()


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


def get_problem_info(url=None):
    """獲取問題資訊"""
    print("\n📝 請輸入問題資訊:")
    
    # 嘗試從 URL 提取問題編號
    problem_slug = None
    if url:
        problem_slug = extract_problem_slug_from_url(url)
        if problem_slug:
            print(f"從 URL 中檢測到問題: {problem_slug}")
    
    # 獲取問題編號
    while True:
        try:
            problem_num = input("問題編號 (如 904, 3477): ").strip()
            if problem_num.isdigit():
                break
            print("請輸入有效的數字編號")
        except EOFError:
            print("\n❌ 互動式輸入失敗")
            sys.exit(1)
    
    # 獲取問題標題
    title_en = input("英文標題 (如 'Fruit Into Baskets'): ").strip()
    title_zh = input("中文標題 (如 '水果成籃'): ").strip()
    
    # 獲取難度
    while True:
        difficulty = input("難度 (Easy/Medium/Hard): ").strip()
        if difficulty.lower() in ['easy', 'medium', 'hard']:
            break
        print("請輸入 Easy, Medium 或 Hard")
    
    # 獲取問題描述
    print("\n📋 請貼上問題描述 (按 Ctrl+D 或連續兩個 Enter 結束):")
    description_lines = []
    empty_line_count = 0
    
    try:
        while True:
            try:
                line = input()
                if line.strip() == "":
                    empty_line_count += 1
                    if empty_line_count >= 2:
                        break
                else:
                    empty_line_count = 0
                description_lines.append(line)
            except EOFError:
                break
    except KeyboardInterrupt:
        print("\n輸入被取消")
        sys.exit(1)
    
    # 處理描述內容
    description = "\n".join(description_lines).strip()
    if not description:
        description = "<!-- 請在此處添加問題描述 -->\n<!-- Please add problem description here -->"
    
    # 嘗試解析範例
    examples = extract_examples_from_description(description)
    
    return {
        'number': problem_num,
        'title_en': title_en,
        'title_zh': title_zh,
        'difficulty': difficulty.capitalize(),
        'slug': problem_slug or f"problem-{problem_num}",
        'description': description,
        'examples': examples
    }


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
"""


def create_markdown_template(problem_info):
    """創建 Markdown 模板"""
    return f"""# {problem_info['number']}. {problem_info['title_en']}

## Problem Description

**Difficulty**: {problem_info['difficulty']}

{problem_info.get('description', default_description_text())}

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

{problem_info.get('examples', default_example_text())}

## Key Points

1. <!-- Key point 1 -->
2. <!-- Key point 2 -->
3. <!-- Key point 3 -->

---

# {problem_info['number']}. {problem_info['title_zh']}

## 問題描述

**難度**: {problem_info['difficulty']}

{problem_info.get('description', default_description_text())}

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

{problem_info.get('examples', default_example_text())}

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
    print("🚀 LeetCode Daily Problem Setup")
    print("=" * 40)
    
    # 檢查是否提供了 URL
    url = sys.argv[1] if len(sys.argv) > 1 else None
    if url:
        print(f"輸入的 URL: {url}")
    
    # 1. 創建今日資料夾
    if not create_daily_folder():
        print("❌ 無法創建今日資料夾，程序結束")
        return
    
    # 2. 獲取問題資訊
    problem_info = get_problem_info(url)
    
    # 3. 確認資料夾路徑
    folder_path = get_today_folder()
    if not os.path.exists(folder_path):
        print(f"❌ 資料夾不存在: {folder_path}")
        return
    
    # 4. 找到舊檔案並重命名
    old_files = [f for f in os.listdir(folder_path) if f.endswith('.py')]
    if not old_files:
        print("❌ 找不到 Python 檔案")
        return
    
    old_num = old_files[0].replace('.py', '')
    py_file, md_file = rename_files(folder_path, old_num, problem_info['number'])
    
    if not py_file or not md_file:
        return
    
    # 5. 更新檔案內容
    if update_files(py_file, md_file, problem_info):
        print("\n🎉 設置完成!")
        print(f"📁 資料夾: {folder_path}")
        print(f"🐍 Python 檔案: {py_file}")
        print(f"📝 Markdown 檔案: {md_file}")
        print("\n💡 提示:")
        print("1. 請根據問題要求修改 Python 檔案中的方法名和參數")
        print("2. 請完善 Markdown 檔案中的問題描述和解題思路")
    else:
        print("❌ 設置失敗")


if __name__ == "__main__":
    main()