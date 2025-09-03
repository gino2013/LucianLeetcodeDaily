from typing import List
from collections import defaultdict

class Solution:
    def numberOfPointsInRectangle(self, points: List[List[int]]) -> int:
        """修復版本：移除有問題的面積剪枝"""
        n = len(points)
        
        if n < 2:
            return 0
        
        # 根據數據規模選擇算法
        if n <= 200:
            return self._optimized_brute_force(points)
        else:
            return self._advanced_sweep_line(points)
    
    def _optimized_brute_force(self, points):
        """優化的暴力算法 - 移除面積剪枝"""
        n = len(points)
        count = 0
        
        for i in range(n):
            alice_x, alice_y = points[i]
            
            for j in range(n):
                if i == j:
                    continue
                
                bob_x, bob_y = points[j]
                
                if alice_x <= bob_x and alice_y >= bob_y:
                    # 直接進行衝突檢測，不進行面積剪枝
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        
                        x, y = points[k]
                        if alice_x <= x <= bob_x and bob_y <= y <= alice_y:
                            valid = False
                            break
                    
                    if valid:
                        count += 1
        
        return count
    
    def _advanced_sweep_line(self, points):
        """高級掃描線算法 - 安全優化版本"""
        n = len(points)
        count = 0
        
        # y座標分組優化
        points_by_y = defaultdict(list)
        for i, (x, y) in enumerate(points):
            points_by_y[y].append((x, i))
        
        # 對每個y的點按x排序
        for y in points_by_y:
            points_by_y[y].sort()
        
        # y座標按降序
        y_coords = sorted(points_by_y.keys(), reverse=True)
        
        # Alice遍歷
        for alice_idx in range(n):
            alice_x, alice_y = points[alice_idx]
            
            # Bob遍歷
            for bob_idx in range(n):
                if alice_idx == bob_idx:
                    continue
                
                bob_x, bob_y = points[bob_idx]
                
                if alice_x > bob_x or alice_y < bob_y:
                    continue
                
                # 安全的衝突檢測：使用索引優化但不預先剪枝
                valid = True
                
                for y in y_coords:
                    if y > alice_y or y < bob_y:
                        continue
                    
                    # 在這個y層級檢查x範圍內的點
                    for x, point_idx in points_by_y[y]:
                        if x > bob_x:
                            break  # 早期終止
                        
                        if x >= alice_x and point_idx != alice_idx and point_idx != bob_idx:
                            valid = False
                            break
                    
                    if not valid:
                        break
                
                if valid:
                    count += 1
        
        return count

# 測試修復效果
def test_fix():
    sol = Solution()
    
    # 失敗案例
    failure_case = [[2,5],[128653,-2370425]]
    result = sol.numberOfPointsInRectangle(failure_case)
    print(f"失敗案例 {failure_case}:")
    print(f"結果: {result} (預期: 1) {'✅' if result == 1 else '❌'}")
    print()
    
    # 其他測試案例
    test_cases = [
        ([[1,1],[2,2],[3,3]], 0),
        ([[6,2],[4,4],[2,6]], 2),
        ([[3,1],[1,3],[1,1]], 2),
        ([[1,2],[3,1]], 1),
        ([], 0),
        ([[1,1]], 0),
    ]
    
    print("其他測試案例:")
    all_pass = True
    for points, expected in test_cases:
        result = sol.numberOfPointsInRectangle(points)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_pass = False
        print(f"  {points} -> {result} (預期: {expected}) {status}")
    
    print(f"\n所有測試 {'通過' if all_pass and sol.numberOfPointsInRectangle(failure_case) == 1 else '失敗'}")

if __name__ == "__main__":
    test_fix()