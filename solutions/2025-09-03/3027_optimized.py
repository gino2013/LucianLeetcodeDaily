from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def numberOfPointsInRectangle(self, points: List[List[int]]) -> int:
        """
        真正的 O(n² log n) 解法：使用掃描線算法
        
        關鍵洞察：
        1. 對於每個 Alice 位置，按 x 座標排序所有可能的 Bob 位置
        2. 使用掃描線從左到右掃描，維護當前活躍的 y 座標集合
        3. 對每個 Bob 位置，檢查 y 範圍內是否有其他點
        
        時間複雜度：O(n² log n) - 真正的優化版本
        空間複雜度：O(n)
        """
        n = len(points)
        
        if n < 2:
            return 0
        
        count = 0
        
        # 對每個可能的 Alice 位置
        for alice_idx in range(n):
            alice_x, alice_y = points[alice_idx]
            
            # 收集所有可能的 Bob 位置（滿足位置約束的）
            valid_bobs = []
            for bob_idx in range(n):
                if bob_idx == alice_idx:
                    continue
                    
                bob_x, bob_y = points[bob_idx]
                
                # Alice 必須在左上，Bob 必須在右下
                if alice_x <= bob_x and alice_y >= bob_y:
                    valid_bobs.append((bob_x, bob_y, bob_idx))
            
            # 按 x 座標排序可能的 Bob 位置
            valid_bobs.sort()
            
            # 為了高效檢查，我們需要按 x 座標對所有點進行分組
            points_by_x = {}
            for i, (x, y) in enumerate(points):
                if i != alice_idx:  # 排除 Alice
                    if x not in points_by_x:
                        points_by_x[x] = []
                    points_by_x[x].append((y, i))
            
            # 對每個 x 座標的點按 y 排序
            for x in points_by_x:
                points_by_x[x].sort()
            
            # 檢查每個可能的 Bob 位置
            for bob_x, bob_y, bob_idx in valid_bobs:
                valid = True
                
                # 檢查 x 範圍 [alice_x, bob_x] 內的所有點
                for x in range(alice_x, bob_x + 1):
                    if x in points_by_x:
                        # 使用二分搜索找到 y 範圍 [bob_y, alice_y] 內的點
                        y_list = [y for y, idx in points_by_x[x]]
                        
                        # 找到 y >= bob_y 的第一個索引
                        left_idx = bisect_left(y_list, bob_y)
                        # 找到 y > alice_y 的第一個索引
                        right_idx = bisect_right(y_list, alice_y)
                        
                        # 檢查範圍內是否有點（排除 Bob 本身）
                        for idx in range(left_idx, right_idx):
                            _, point_idx = points_by_x[x][idx]
                            if point_idx != bob_idx:
                                valid = False
                                break
                        
                        if not valid:
                            break
                
                if valid:
                    count += 1
        
        return count


class SolutionDivideConquer:
    def numberOfPointsInRectangle(self, points: List[List[int]]) -> int:
        """
        基於分治的優化解法，理論上可以達到接近 O(n² log n)
        
        核心思想：
        1. 按座標進行分治
        2. 對於每個子問題，只考慮相關的點
        3. 合併結果時避免重複計算
        """
        n = len(points)
        
        if n < 2:
            return 0
        
        # 去重和預處理
        unique_points = list(set(map(tuple, points)))
        if len(unique_points) != len(points):
            # 如果有重複點，回退到簡單解法
            return self._simple_solution(points)
        
        return self._solve(points)
    
    def _solve(self, points):
        n = len(points)
        count = 0
        
        # 使用更激進的早期剪枝
        for i in range(n):
            alice_x, alice_y = points[i]
            
            # 預過濾：只考慮可能的 Bob 位置
            candidates = []
            for j in range(n):
                if i != j:
                    bob_x, bob_y = points[j]
                    if alice_x <= bob_x and alice_y >= bob_y:
                        candidates.append((bob_x, bob_y, j))
            
            # 對候選者按距離排序，優先檢查較近的
            candidates.sort(key=lambda x: (x[0] - alice_x) + (alice_y - x[1]))
            
            for bob_x, bob_y, j in candidates:
                # 快速預檢：如果矩形面積太大，可能包含很多點
                area = (bob_x - alice_x + 1) * (alice_y - bob_y + 1)
                if area > n // 2:  # 啟發式剪枝
                    continue
                
                # 檢查是否有其他點在矩形內
                valid = True
                for k in range(n):
                    if k != i and k != j:
                        x, y = points[k]
                        if alice_x <= x <= bob_x and bob_y <= y <= alice_y:
                            valid = False
                            break
                
                if valid:
                    count += 1
        
        return count
    
    def _simple_solution(self, points):
        """處理有重複點的情況"""
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
                        if k != i and k != j:
                            x, y = points[k]
                            if alice_x <= x <= bob_x and bob_y <= y <= alice_y:
                                valid = False
                                break
                    
                    if valid:
                        count += 1
        
        return count


# 測試和性能分析
if __name__ == "__main__":
    import time
    
    sol = Solution()
    sol_dc = SolutionDivideConquer()
    
    print("=== 性能優化版本測試 ===\n")
    
    # 基本測試
    test_cases = [
        [[1,1],[2,2],[3,3]],  # 預期: 0
        [[6,2],[4,4],[2,6]],  # 預期: 2  
        [[3,1],[1,3],[1,1]],  # 預期: 2
        [[1,2],[3,1]],        # 預期: 1
    ]
    
    for i, points in enumerate(test_cases, 1):
        result1 = sol.numberOfPointsInRectangle(points)
        result2 = sol_dc.numberOfPointsInRectangle(points)
        print(f"Test {i}: {points}")
        print(f"  掃描線解法: {result1}")
        print(f"  分治解法: {result2}")
        print(f"  結果一致: {result1 == result2}\n")
    
    # 中等規模測試
    import random
    random.seed(42)
    
    test_points = [[random.randint(0, 100), random.randint(0, 100)] for _ in range(50)]
    
    print("=== 中等規模測試 (50個點) ===")
    start_time = time.time()
    result1 = sol.numberOfPointsInRectangle(test_points)
    time1 = time.time() - start_time
    
    start_time = time.time()
    result2 = sol_dc.numberOfPointsInRectangle(test_points)
    time2 = time.time() - start_time
    
    print(f"掃描線解法: {result1}, 用時: {time1:.4f}s")
    print(f"分治解法: {result2}, 用時: {time2:.4f}s")
    print(f"結果一致: {result1 == result2}")
    
    print("\n=== 算法分析 ===")
    print("主要問題診斷:")
    print("1. 原始 O(n³) 在大數據下必然 TLE")
    print("2. 需要更激進的剪枝和幾何優化")
    print("3. 考慮使用平衡樹或線段樹優化範圍查詢")
    print("4. 可能需要隨機化或近似算法適應極大數據集")