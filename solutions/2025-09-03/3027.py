from typing import List

class Solution:
    def numberOfPointsInRectangle(self, points: List[List[int]]) -> int:
        """
        最優解法：座標壓縮 + 前綴和矩陣
        
        核心思想：
        1. 座標壓縮：將稀疏座標映射到密集空間，避免巨大矩陣
        2. 前綴和矩陣：O(1) 時間查詢任意矩形內的點數量
        3. 智能枚舉：按 x 升序、y 降序排列，確保正確的 Alice-Bob 順序
        4. 高效驗證：只需檢查矩形內是否恰好有 2 個點（Alice 和 Bob）
        
        時間複雜度：O(n² + n log n)
        空間複雜度：O(n²)
        
        這個方法完全避免了複雜的剪枝邏輯，從根本上提高了效率
        """
        if len(points) < 2:
            return 0
        
        # 步驟1：座標壓縮
        x_coords = {}  # 原始 x 座標 -> 壓縮索引
        y_coords = {}  # 原始 y 座標 -> 壓縮索引
        
        # 收集所有唯一座標
        for x, y in points:
            x_coords[x] = 0
            y_coords[y] = 0
        
        # 將座標映射到 [1, n] 範圍（從 1 開始便於前綴和計算）
        def compress_coordinates(coord_map):
            sorted_coords = sorted(coord_map.keys())
            for i, coord in enumerate(sorted_coords):
                coord_map[coord] = i + 1
        
        compress_coordinates(x_coords)
        compress_coordinates(y_coords)
        
        # 步驟2：建立網格和座標映射
        max_x = len(x_coords) + 1
        max_y = len(y_coords) + 1
        grid = [[0] * max_y for _ in range(max_x)]
        point_to_compressed = {}
        
        for x, y in points:
            compressed_x = x_coords[x]
            compressed_y = y_coords[y]
            grid[compressed_x][compressed_y] = 1
            point_to_compressed[(x, y)] = (compressed_x, compressed_y)
        
        # 步驟3：構建前綴和矩陣，實現 O(1) 範圍查詢
        prefix_sum = [[0] * max_y for _ in range(max_x)]
        
        for i in range(1, max_x):
            for j in range(1, max_y):
                prefix_sum[i][j] = (
                    prefix_sum[i-1][j] + 
                    prefix_sum[i][j-1] - 
                    prefix_sum[i-1][j-1] + 
                    grid[i][j]
                )
        
        # 步驟4：智能排序 - 按 x 升序，y 降序
        # 這確保了對於 i < j，points[i] 可以作為 Alice，points[j] 可以作為 Bob
        points.sort(key=lambda p: (p[0], -p[1]))
        
        count = 0
        n = len(points)
        
        # 步驟5：枚舉所有可能的 Alice-Bob 對
        for i in range(n - 1):
            alice_x, alice_y = points[i]
            
            for j in range(i + 1, n):
                bob_x, bob_y = points[j]
                
                # 位置約束：Alice 在左上，Bob 在右下
                if alice_x <= bob_x and alice_y >= bob_y:
                    # 獲取壓縮座標
                    alice_cx, alice_cy = point_to_compressed[(alice_x, alice_y)]
                    bob_cx, bob_cy = point_to_compressed[(bob_x, bob_y)]
                    
                    # 使用前綴和計算矩形內點數
                    points_in_rect = (
                        prefix_sum[bob_cx][alice_cy] -
                        prefix_sum[alice_cx - 1][alice_cy] -
                        prefix_sum[bob_cx][bob_cy - 1] +
                        prefix_sum[alice_cx - 1][bob_cy - 1]
                    )
                    
                    # 如果矩形內恰好有 2 個點，說明除了 Alice 和 Bob 沒有其他點
                    if points_in_rect == 2:
                        count += 1
        
        return count


# 綜合測試案例
if __name__ == "__main__":
    sol = Solution()
    
    print("=== LeetCode 3027: Find the Number of Ways to Place People II ===")
    print("最優算法：座標壓縮 + 前綴和矩陣")
    print("時間複雜度: O(n² + n log n)")
    print("空間複雜度: O(n²)\n")
    
    # Test case 1: 基本案例 - 無法形成有效矩形
    points1 = [[1,1],[2,2],[3,3]]
    result1 = sol.numberOfPointsInRectangle(points1)
    print(f"Test 1: {points1}")
    print(f"結果: {result1} (預期: 0)")
    print(f"說明: 所有點都在對角線上，無法形成Alice在左上、Bob在右下的配置\n")
    
    # Test case 2: 基本案例 - 有效配置
    points2 = [[6,2],[4,4],[2,6]]
    result2 = sol.numberOfPointsInRectangle(points2)
    print(f"Test 2: {points2}")
    print(f"結果: {result2} (預期: 2)")
    print(f"說明: 可以有兩種配置：Alice(4,4)Bob(6,2) 和 Alice(2,6)Bob(4,4)\n")
    
    # Test case 3: 邊界情況 - 點在邊界上
    points3 = [[3,1],[1,3],[1,1]]
    result3 = sol.numberOfPointsInRectangle(points3)
    print(f"Test 3: {points3}")
    print(f"結果: {result3} (預期: 2)")
    print(f"說明: Alice(1,1)Bob(3,1) 和 Alice(1,3)Bob(1,1)，注意邊界點會被排除\n")
    
    # Test case 4: Edge case - 空輸入
    points4 = []
    result4 = sol.numberOfPointsInRectangle(points4)
    print(f"Test 4: {points4}")
    print(f"結果: {result4} (預期: 0)")
    print(f"說明: 空輸入，無法形成配對\n")
    
    # Test case 5: Edge case - 單個點
    points5 = [[1,1]]
    result5 = sol.numberOfPointsInRectangle(points5)
    print(f"Test 5: {points5}")
    print(f"結果: {result5} (預期: 0)")
    print(f"說明: 只有一個點，無法形成配對\n")
    
    # Test case 6: Edge case - 兩個點
    points6 = [[1,2],[3,1]]
    result6 = sol.numberOfPointsInRectangle(points6)
    print(f"Test 6: {points6}")
    print(f"結果: {result6} (預期: 1)")
    print(f"說明: Alice(1,2)Bob(3,1)，沒有其他點干擾\n")
    
    # Test case 7: 關鍵案例 - 稀疏大矩形
    points7 = [[2,5],[128653,-2370425]]
    result7 = sol.numberOfPointsInRectangle(points7)
    print(f"Test 7: {points7}")
    print(f"結果: {result7} (預期: 1)")
    print(f"說明: 稀疏大矩形，之前的面積剪枝會錯誤排除\n")
    
    # Test case 8: 複雜案例 - 重複座標
    points8 = [[1,1],[1,1],[2,2]]
    result8 = sol.numberOfPointsInRectangle(points8)
    print(f"Test 8: {points8}")
    print(f"結果: {result8} (實際結果)")
    print(f"說明: 有重複點，但算法將其視為不同的點索引處理\n")
    
    print("=== 複雜度分析 (最優版本) ===")
    print("時間複雜度: O(n² + n log n)")
    print("  - 座標壓縮: O(n log n)")
    print("  - 前綴和構建: O(unique_x × unique_y) ≤ O(n²)")
    print("  - 點對枚舉: O(n²)")
    print("  - 每次範圍查詢: O(1)")
    print("空間複雜度: O(n²)")
    print("  - 座標映射: O(n)")
    print("  - 網格矩陣: O(unique_x × unique_y) ≤ O(n²)")
    print("  - 前綴和矩陣: O(unique_x × unique_y) ≤ O(n²)")
    
    print("\n=== 算法特點 (座標壓縮版) ===")
    print("🎯 座標壓縮：自動處理稀疏座標，無需手動優化")
    print("⚡ 前綴和查詢：O(1) 範圍查詢，徹底避免 O(n) 遍歷")
    print("📊 智能排序：確保枚舉順序，減少無效檢查")
    print("🔧 空間換時間：以 O(n²) 空間獲得理論最優時間複雜度")
    print("✅ 無需剪枝：算法本質高效，避免複雜的邊界情況處理")
    print("🏆 理論最優：在不使用高級數據結構的前提下的最佳解法")
    print("🎖️ 生產就緒：穩定可靠，適用於所有測試案例")