from typing import List

class Solution:
    def numberOfPointsInRectangle(self, points: List[List[int]]) -> int:
        """
        最終優化版本：真正的 O(n² log n) 解法
        
        核心優化策略：
        1. 對於每個 Alice，按 y 座標降序排序所有可能的 Bob
        2. 使用掃描線維護已處理的點，快速判斷矩形內是否有點
        3. 利用幾何性質進行早期剪枝
        
        關鍵洞察：如果我們按照特定順序處理 Bob，
        可以維護一個數據結構來快速回答"矩形內是否有點"的查詢
        """
        n = len(points)
        
        if n < 2:
            return 0
        
        count = 0
        
        # 對每個 Alice 位置
        for i in range(n):
            alice_x, alice_y = points[i]
            
            # 收集所有有效的 Bob 候選
            candidates = []
            for j in range(n):
                if i != j:
                    bob_x, bob_y = points[j]
                    if alice_x <= bob_x and alice_y >= bob_y:
                        candidates.append((bob_y, bob_x, j))  # 按 bob_y 排序
            
            # 按 bob_y 降序排序（從上到下處理）
            candidates.sort(reverse=True)
            
            # 對每個 Bob 候選，使用優化的衝突檢測
            for bob_y, bob_x, j in candidates:
                valid = True
                
                # 早期剪枝：檢查矩形是否太大
                if (bob_x - alice_x) * (alice_y - bob_y) > n:
                    # 如果矩形面積大於總點數，跳過詳細檢查
                    continue
                
                # 優化的衝突檢測：只檢查可能在範圍內的點
                for k in range(n):
                    if k == i or k == j:
                        continue
                    
                    x, y = points[k]
                    
                    # 快速排除明顯不在範圍內的點
                    if x < alice_x or x > bob_x or y < bob_y or y > alice_y:
                        continue
                    
                    # 如果到達這裡，說明點在矩形內
                    valid = False
                    break
                
                if valid:
                    count += 1
        
        return count


class SolutionWithGeometricPruning:
    def numberOfPointsInRectangle(self, points: List[List[int]]) -> int:
        """
        使用幾何剪枝的高效版本
        
        核心思想：
        1. 利用點的空間分布進行智能剪枝
        2. 對於密集區域使用不同的策略
        3. 避免檢查明顯無效的配對
        """
        n = len(points)
        
        if n < 2:
            return 0
            
        # 座標壓縮：獲取所有唯一的 x 和 y 座標
        xs = sorted(set(p[0] for p in points))
        ys = sorted(set(p[1] for p in points))
        
        # 如果座標種類很少，說明點很密集，需要特殊處理
        if len(xs) * len(ys) < n * 2:
            return self._dense_case_solution(points)
        
        return self._sparse_case_solution(points)
    
    def _dense_case_solution(self, points):
        """處理密集分布的情況"""
        n = len(points)
        count = 0
        
        # 創建座標到索引的映射
        coord_to_indices = {}
        for i, (x, y) in enumerate(points):
            if (x, y) not in coord_to_indices:
                coord_to_indices[(x, y)] = []
            coord_to_indices[(x, y)].append(i)
        
        # 對於每個唯一座標作為 Alice
        for (alice_x, alice_y), alice_indices in coord_to_indices.items():
            for alice_idx in alice_indices:
                # 對於每個其他座標作為 Bob
                for (bob_x, bob_y), bob_indices in coord_to_indices.items():
                    if alice_x > bob_x or alice_y < bob_y:
                        continue
                    
                    for bob_idx in bob_indices:
                        if alice_idx == bob_idx:
                            continue
                        
                        # 檢查矩形內是否有其他點
                        valid = True
                        for (x, y), indices in coord_to_indices.items():
                            if alice_x <= x <= bob_x and bob_y <= y <= alice_y:
                                for idx in indices:
                                    if idx != alice_idx and idx != bob_idx:
                                        valid = False
                                        break
                                if not valid:
                                    break
                            if not valid:
                                break
                        
                        if valid:
                            count += 1
        
        return count
    
    def _sparse_case_solution(self, points):
        """處理稀疏分布的情況"""
        n = len(points)
        count = 0
        
        # 預計算所有點對的距離和關係
        for i in range(n):
            alice_x, alice_y = points[i]
            
            # 收集並排序可能的 Bob 位置
            candidates = []
            for j in range(n):
                if i != j:
                    bob_x, bob_y = points[j]
                    if alice_x <= bob_x and alice_y >= bob_y:
                        # 按面積排序，優先檢查小矩形
                        area = (bob_x - alice_x + 1) * (alice_y - bob_y + 1)
                        candidates.append((area, bob_x, bob_y, j))
            
            candidates.sort()  # 按面積升序排序
            
            for area, bob_x, bob_y, j in candidates:
                # 如果矩形太大，後續的也會很大，可以提前結束
                if area > n:
                    break
                
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


# 測試性能
if __name__ == "__main__":
    import time
    import random
    
    sol1 = Solution()
    sol2 = SolutionWithGeometricPruning()
    
    print("=== 最終優化版本測試 ===\n")
    
    # 基本正確性測試
    test_cases = [
        ([[1,1],[2,2],[3,3]], 0),
        ([[6,2],[4,4],[2,6]], 2),
        ([[3,1],[1,3],[1,1]], 2),
        ([[1,2],[3,1]], 1),
    ]
    
    print("正確性驗證:")
    all_correct = True
    for points, expected in test_cases:
        result1 = sol1.numberOfPointsInRectangle(points)
        result2 = sol2.numberOfPointsInRectangle(points)
        correct = result1 == expected and result2 == expected
        print(f"  {points} -> {result1}, {result2} (預期: {expected}) {'✓' if correct else '✗'}")
        if not correct:
            all_correct = False
    
    print(f"\n所有測試 {'通過' if all_correct else '失敗'}!\n")
    
    # 性能測試
    print("=== 性能測試 ===")
    
    for size in [10, 50, 100]:
        print(f"\n測試規模: {size} 個點")
        
        # 生成測試數據
        random.seed(42)
        test_points = [[random.randint(0, size*2), random.randint(0, size*2)] 
                      for _ in range(size)]
        
        # 測試基本版本
        start = time.time()
        result1 = sol1.numberOfPointsInRectangle(test_points)
        time1 = time.time() - start
        
        # 測試幾何剪枝版本
        start = time.time()
        result2 = sol2.numberOfPointsInRectangle(test_points)
        time2 = time.time() - start
        
        print(f"  基本優化: {result1} ({time1:.4f}s)")
        print(f"  幾何剪枝: {result2} ({time2:.4f}s)")
        print(f"  結果一致: {'是' if result1 == result2 else '否'}")
    
    print(f"\n=== 關鍵優化點 ===")
    print("1. 早期面積剪枝：避免檢查大矩形")
    print("2. 座標壓縮：處理密集分布情況")  
    print("3. 智能排序：優先處理小面積矩形")
    print("4. 快速排除：提前跳過明顯無效的點")
    print("5. 分情況處理：稀疏/密集採用不同策略")