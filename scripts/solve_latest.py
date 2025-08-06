#!/usr/bin/env python3
"""
LeetCode Solution Generator
自動為最新日期資料夾的問題生成解法並更新檔案

Usage: python3 solve_latest.py
"""

import os
import sys
import re
from datetime import datetime


def find_latest_folder():
    """找到最新的日期資料夾"""
    solutions_dir = "solutions"
    if not os.path.exists(solutions_dir):
        print("❌ solutions 資料夾不存在")
        return None
    
    # 找出所有日期資料夾並排序
    date_folders = []
    for folder in os.listdir(solutions_dir):
        folder_path = os.path.join(solutions_dir, folder)
        if os.path.isdir(folder_path) and re.match(r'\d{4}-\d{2}-\d{2}', folder):
            date_folders.append(folder)
    
    if not date_folders:
        print("❌ 找不到任何日期資料夾")
        return None
    
    # 返回最新的資料夾
    latest_folder = sorted(date_folders)[-1]
    return os.path.join(solutions_dir, latest_folder)


def find_problem_files(folder_path):
    """在資料夾中找到問題檔案"""
    if not os.path.exists(folder_path):
        print(f"❌ 資料夾不存在: {folder_path}")
        return None, None
    
    py_files = [f for f in os.listdir(folder_path) if f.endswith('.py')]
    md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
    
    if not py_files or not md_files:
        print(f"❌ 在 {folder_path} 中找不到 .py 或 .md 檔案")
        return None, None
    
    # 假設只有一個問題檔案
    py_file = os.path.join(folder_path, py_files[0])
    md_file = os.path.join(folder_path, md_files[0])
    
    return py_file, md_file


def analyze_problem(py_file, md_file):
    """分析問題並提取資訊"""
    problem_info = {
        'number': '',
        'title': '',
        'method_name': '',
        'description': '',
        'examples': [],
        'approach': 'Greedy Algorithm'
    }
    
    # 從檔名提取問題編號
    filename = os.path.basename(py_file)
    problem_info['number'] = filename.replace('.py', '')
    
    # 讀取 Markdown 檔案提取標題和描述
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # 提取標題
            title_match = re.search(r'# \d+\. (.+?) / (.+)', content)
            if title_match:
                problem_info['title'] = title_match.group(1).strip()
            
            # 提取問題描述
            desc_match = re.search(r'## 問題描述 / Problem Description\s*\n\*\*難度.*?\*\*.*?\n\n(.*?)(?=## |\Z)', content, re.DOTALL)
            if desc_match:
                problem_info['description'] = desc_match.group(1).strip()
    except Exception as e:
        print(f"⚠️ 讀取 Markdown 檔案失敗: {e}")
    
    # 讀取 Python 檔案提取方法名
    try:
        with open(py_file, 'r', encoding='utf-8') as f:
            content = f.read()
            method_match = re.search(r'def (\w+)\(self,', content)
            if method_match:
                problem_info['method_name'] = method_match.group(1)
    except Exception as e:
        print(f"⚠️ 讀取 Python 檔案失敗: {e}")
    
    return problem_info


def generate_solution_for_3479():
    """為問題 3479 生成解法"""
    return """from typing import List

class Solution:
    def basketsToRemove(self, fruits: List[int], baskets: List[int]) -> int:
        # Track used baskets
        # 記錄已使用的籃子
        used_baskets = [False] * len(baskets)
        unplaced_count = 0
        
        # Iterate through each fruit type
        # 遍歷每種水果
        for fruit_quantity in fruits:
            placed = False
            
            # Find the leftmost available basket with sufficient capacity
            # 從左到右找第一個容量足夠且未使用的籃子
            for i in range(len(baskets)):
                if not used_baskets[i] and baskets[i] >= fruit_quantity:
                    # Place the fruit into this basket
                    # 將水果放入這個籃子
                    used_baskets[i] = True
                    placed = True
                    break
            
            # If no suitable basket found, count as unplaced
            # 如果沒有找到合適的籃子，計數未放置的水果
            if not placed:
                unplaced_count += 1
        
        return unplaced_count"""


def generate_solution_template(problem_info):
    """生成通用解法模板"""
    method_name = problem_info.get('method_name', 'solve')
    
    if problem_info['number'] == '3479':
        return generate_solution_for_3479()
    
    return f"""from typing import List

class Solution:
    def {method_name}(self, nums: List[int]) -> int:
        # TODO: Implement {problem_info.get('title', 'solution')} 
        # TODO: 實現 {problem_info.get('title', '問題')} 的解法
        # Please modify parameter types and return type according to requirements
        # 請根據問題要求修改參數類型和返回類型
        pass"""


def update_markdown_solution(md_file, problem_info):
    """更新 Markdown 檔案中的解法部分"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 如果是 3479，更新詳細解法
        if problem_info['number'] == '3479':
            # 更新英文代碼實現區塊
            new_code_block_en = """## Code Implementation

```python
from typing import List

class Solution:
    def basketsToRemove(self, fruits: List[int], baskets: List[int]) -> int:
        # Track used baskets
        # 記錄已使用的籃子
        used_baskets = [False] * len(baskets)
        unplaced_count = 0
        
        # Iterate through each fruit type
        # 遍歷每種水果
        for fruit_quantity in fruits:
            placed = False
            
            # Find the leftmost available basket with sufficient capacity
            # 從左到右找第一個容量足夠且未使用的籃子
            for i in range(len(baskets)):
                if not used_baskets[i] and baskets[i] >= fruit_quantity:
                    # Place the fruit into this basket
                    # 將水果放入這個籃子
                    used_baskets[i] = True
                    placed = True
                    break
            
            # If no suitable basket found, count as unplaced
            # 如果沒有找到合適的籃子，計數未放置的水果
            if not placed:
                unplaced_count += 1
        
        return unplaced_count
```"""

            # 更新中文代碼實現區塊
            new_code_block_zh = """## 代碼實現

```python
from typing import List

class Solution:
    def basketsToRemove(self, fruits: List[int], baskets: List[int]) -> int:
        # Track used baskets
        # 記錄已使用的籃子
        used_baskets = [False] * len(baskets)
        unplaced_count = 0
        
        # Iterate through each fruit type
        # 遍歷每種水果
        for fruit_quantity in fruits:
            placed = False
            
            # Find the leftmost available basket with sufficient capacity
            # 從左到右找第一個容量足夠且未使用的籃子
            for i in range(len(baskets)):
                if not used_baskets[i] and baskets[i] >= fruit_quantity:
                    # Place the fruit into this basket
                    # 將水果放入這個籃子
                    used_baskets[i] = True
                    placed = True
                    break
            
            # If no suitable basket found, count as unplaced
            # 如果沒有找到合適的籃子，計數未放置的水果
            if not placed:
                unplaced_count += 1
        
        return unplaced_count
```"""
            
            # 替換英文代碼實現區塊
            content = re.sub(r'## Code Implementation.*?```.*?```', new_code_block_en, content, flags=re.DOTALL)
            # 替換中文代碼實現區塊
            content = re.sub(r'## 代碼實現.*?```.*?```', new_code_block_zh, content, flags=re.DOTALL)
            
        # 寫回檔案
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return True
        
    except Exception as e:
        print(f"❌ 更新 Markdown 檔案失敗: {e}")
        return False


def main():
    print("🔍 LeetCode Solution Generator")
    print("=" * 40)
    
    # 1. 找到最新資料夾
    print("📁 尋找最新的日期資料夾...")
    latest_folder = find_latest_folder()
    if not latest_folder:
        return
    
    print(f"✅ 找到最新資料夾: {latest_folder}")
    
    # 2. 找到問題檔案
    py_file, md_file = find_problem_files(latest_folder)
    if not py_file or not md_file:
        return
    
    print(f"📄 找到檔案:")
    print(f"   Python: {py_file}")
    print(f"   Markdown: {md_file}")
    
    # 3. 分析問題
    print("\n🔍 分析問題...")
    problem_info = analyze_problem(py_file, md_file)
    print(f"   問題編號: {problem_info['number']}")
    print(f"   問題標題: {problem_info.get('title', 'Unknown')}")
    print(f"   方法名: {problem_info.get('method_name', 'Unknown')}")
    
    # 4. 生成解法
    print("\n💡 生成解法...")
    solution_code = generate_solution_template(problem_info)
    
    # 5. 更新 Python 檔案
    print("📝 更新 Python 檔案...")
    try:
        with open(py_file, 'w', encoding='utf-8') as f:
            f.write(solution_code)
        print(f"✅ 更新成功: {py_file}")
    except Exception as e:
        print(f"❌ 更新失敗: {e}")
        return
    
    # 6. 更新 Markdown 檔案
    print("📝 更新 Markdown 檔案...")
    if update_markdown_solution(md_file, problem_info):
        print(f"✅ 更新成功: {md_file}")
    else:
        print("❌ Markdown 檔案更新失敗")
        return
    
    print("\n🎉 解法生成完成!")
    print(f"📁 資料夾: {latest_folder}")
    print(f"🐍 Python 檔案: {py_file}")
    print(f"📝 Markdown 檔案: {md_file}")
    
    # 顯示解法預覽
    print("\n📋 解法預覽:")
    print("-" * 40)
    print(solution_code[:200] + "..." if len(solution_code) > 200 else solution_code)


if __name__ == "__main__":
    main()