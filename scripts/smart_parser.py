#!/usr/bin/env python3
"""
Smart LeetCode Problem Parser
智能 LeetCode 題目解析器
"""

import re
import sys
from typing import Dict, Optional


def extract_problem_number(text: str) -> Optional[str]:
    """提取題目編號"""
    # 尋找 "2787. Ways to Express" 格式
    pattern = r'(?:^|\n)(\d+)\.\s+'
    match = re.search(pattern, text, re.MULTILINE)
    if match:
        return match.group(1)
    
    # 尋找其他可能的編號格式
    patterns = [
        r'Problem\s+(\d+)',
        r'LeetCode\s+(\d+)',
        r'#(\d+)',
        r'題目\s*(\d+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
    
    return None


def extract_title(text: str, problem_number: str = None) -> tuple[Optional[str], Optional[str]]:
    """提取英文和中文標題"""
    english_title = None
    chinese_title = None
    
    if problem_number:
        # 尋找 "編號. 標題" 格式
        pattern = rf'{problem_number}\.\s*(.+?)(?:\n|$)'
        match = re.search(pattern, text)
        if match:
            title_line = match.group(1).strip()
            
            # 檢查是否包含中文字符
            if re.search(r'[\u4e00-\u9fff]', title_line):
                chinese_title = title_line
            else:
                english_title = title_line
    
    # 嘗試其他方式提取標題
    if not english_title and not chinese_title:
        # 尋找可能的標題行
        lines = text.split('\n')
        for line in lines[:10]:  # 只檢查前10行
            line = line.strip()
            if not line or line.startswith('Given') or line.startswith('Return'):
                continue
            
            # 移除可能的編號前綴
            clean_line = re.sub(r'^\d+\.\s*', '', line)
            
            if re.search(r'[\u4e00-\u9fff]', clean_line):
                if not chinese_title and len(clean_line) < 100:
                    chinese_title = clean_line
            else:
                if not english_title and len(clean_line) < 100 and clean_line[0].isupper():
                    english_title = clean_line
    
    return english_title, chinese_title


def extract_difficulty(text: str) -> str:
    """提取難度"""
    # 尋找難度關鍵詞
    patterns = [
        r'(?:Difficulty|難度)[:：]\s*(Easy|Medium|Hard|簡單|中等|困難)',
        r'\b(Easy|Medium|Hard|簡單|中等|困難)\b'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            difficulty = match.group(1).lower()
            difficulty_map = {
                'easy': 'Easy',
                'medium': 'Medium', 
                'hard': 'Hard',
                '簡單': 'Easy',
                '中等': 'Medium',
                '困難': 'Hard'
            }
            return difficulty_map.get(difficulty, 'Medium')
    
    return 'Medium'  # 默認中等


def extract_examples(text: str) -> str:
    """提取範例"""
    examples = []
    
    # 尋找 Example 1:, Example 2: 等
    example_pattern = r'Example\s+(\d+):(.*?)(?=Example\s+\d+:|Constraints:|$)'
    matches = re.findall(example_pattern, text, re.DOTALL | re.IGNORECASE)
    
    if matches:
        example_text = ""
        for num, content in matches:
            content = content.strip()
            example_text += f"**Example {num}:**\n```\n{content}\n```\n\n"
        return example_text.strip()
    
    return '''**Example 1:**
```
Input: 
Output: 
Explanation: 
```'''


def clean_description(text: str) -> str:
    """清理問題描述"""
    # 移除一些常見的非描述內容
    lines = text.split('\n')
    cleaned_lines = []
    
    skip_patterns = [
        r'^\s*Example\s+\d+:',
        r'^\s*Constraints:',
        r'^\s*Follow up:',
        r'^\s*Note:',
        r'^\s*提示:',
        r'^\s*範例\s*\d+:',
    ]
    
    in_constraints = False
    
    for line in lines:
        # 跳過約束條件之後的內容
        if re.search(r'^\s*Constraints:', line, re.IGNORECASE):
            in_constraints = True
            continue
        
        if in_constraints:
            continue
            
        # 跳過範例內容
        skip = False
        for pattern in skip_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                skip = True
                break
        
        if not skip and line.strip():
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines).strip()


def parse_problem(text: str) -> Dict[str, str]:
    """解析完整的題目信息"""
    problem_number = extract_problem_number(text)
    english_title, chinese_title = extract_title(text, problem_number)
    difficulty = extract_difficulty(text)
    examples = extract_examples(text)
    description = clean_description(text)
    
    return {
        'number': problem_number or '0000',
        'title_en': english_title or 'Unknown Problem',
        'title_zh': chinese_title or '未知問題',
        'difficulty': difficulty,
        'examples': examples,
        'description': description,
        'slug': f"problem-{problem_number}" if problem_number else "unknown-problem"
    }


if __name__ == "__main__":
    # 測試功能
    if len(sys.argv) > 1:
        test_text = sys.argv[1]
    else:
        test_text = sys.stdin.read()
    
    result = parse_problem(test_text)
    
    print("解析結果:")
    for key, value in result.items():
        print(f"{key}: {value}")