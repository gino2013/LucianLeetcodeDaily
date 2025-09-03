from typing import List
from collections import defaultdict

def debug_case(points, expected):
    """調試特定測試案例"""
    print(f"\n=== 調試案例: {points} (預期: {expected}) ===")
    
    # 原始暴力算法（正確）
    def brute_force(points):
        n = len(points)
        count = 0
        
        for i in range(n):
            alice_x, alice_y = points[i]
            
            for j in range(n):
                if i == j:
                    continue
                
                bob_x, bob_y = points[j]
                
                if alice_x <= bob_x and alice_y >= bob_y:
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        
                        x, y = points[k]
                        if alice_x <= x <= bob_x and bob_y <= y <= alice_y:
                            valid = False
                            break
                    
                    if valid:
                        print(f"  有效配對: Alice({alice_x},{alice_y}) Bob({bob_x},{bob_y})")
                        count += 1
        
        return count
    
    result = brute_force(points)
    print(f"暴力算法結果: {result}")
    return result == expected

# 測試所有案例
test_cases = [
    ([[6,2],[4,4],[2,6]], 2),
    ([[1,2],[3,1]], 1),
]

for points, expected in test_cases:
    debug_case(points, expected)