from typing import List

class Solution:
    def numberOfPointsInRectangle(self, points: List[List[int]]) -> int:
        """
        最優解法：座標壓縮 + 前綴和 + 智能枚舉
        
        核心思想：
        1. 座標壓縮：將所有 x,y 座標映射到 [1, n] 範圍內
        2. 前綴和矩陣：快速計算任意矩形區域內的點數量
        3. 智能枚舉：按特定順序枚舉點對，確保 Alice 在左上、Bob 在右下
        4. O(1) 範圍查詢：使用前綴和在常數時間內檢查矩形內點數
        
        時間複雜度：O(n² + n log n)
        空間複雜度：O(n²) 用於前綴和矩陣
        """
        if len(points) < 2:
            return 0
        
        # 步驟1：座標壓縮
        x_coords = {}  # 原始x座標 -> 壓縮後的索引
        y_coords = {}  # 原始y座標 -> 壓縮後的索引
        
        # 收集所有唯一的座標
        for x, y in points:
            x_coords[x] = 0
            y_coords[y] = 0
        
        # 將座標映射到 [1, n] 範圍（從1開始，方便前綴和計算）
        def compress_coordinates(coord_map):
            sorted_coords = sorted(coord_map.keys())
            for i, coord in enumerate(sorted_coords):
                coord_map[coord] = i + 1
        
        compress_coordinates(x_coords)
        compress_coordinates(y_coords)
        
        # 步驟2：建立點存在矩陣和座標映射
        max_x = len(x_coords) + 1
        max_y = len(y_coords) + 1
        grid = [[0] * max_y for _ in range(max_x)]
        point_to_compressed = {}
        
        for x, y in points:
            compressed_x = x_coords[x]
            compressed_y = y_coords[y]
            grid[compressed_x][compressed_y] = 1
            point_to_compressed[(x, y)] = (compressed_x, compressed_y)
        
        # 步驟3：構建前綴和矩陣，用於 O(1) 範圍查詢
        prefix_sum = [[0] * max_y for _ in range(max_x)]
        
        for i in range(1, max_x):
            for j in range(1, max_y):
                prefix_sum[i][j] = (
                    prefix_sum[i-1][j] + 
                    prefix_sum[i][j-1] - 
                    prefix_sum[i-1][j-1] + 
                    grid[i][j]
                )
        
        # 步驟4：智能枚舉 - 按 x 升序, y 降序排序
        # 這樣確保對於任何 i < j，points[i] 都可能是 Alice，points[j] 可能是 Bob
        points.sort(key=lambda p: (p[0], -p[1]))
        
        count = 0
        n = len(points)
        
        # 步驟5：枚舉所有可能的 Alice-Bob 對
        for i in range(n - 1):
            alice_x, alice_y = points[i]
            
            for j in range(i + 1, n):
                bob_x, bob_y = points[j]
                
                # 檢查位置約束：Alice 必須在左上，Bob 在右下
                if alice_x <= bob_x and alice_y >= bob_y:
                    # 獲取壓縮座標
                    alice_cx, alice_cy = point_to_compressed[(alice_x, alice_y)]
                    bob_cx, bob_cy = point_to_compressed[(bob_x, bob_y)]
                    
                    # 使用前綴和計算矩形 [alice_x, bob_x] × [bob_y, alice_y] 內的點數
                    points_in_rect = (
                        prefix_sum[bob_cx][alice_cy] -
                        prefix_sum[alice_cx - 1][alice_cy] -
                        prefix_sum[bob_cx][bob_cy - 1] +
                        prefix_sum[alice_cx - 1][bob_cy - 1]
                    )
                    
                    # 如果矩形內只有 Alice 和 Bob 這兩個點，則是有效配對
                    if points_in_rect == 2:
                        count += 1
        
        return count


class SolutionDebug:
    """帶調試功能的版本"""
    def numberOfPointsInRectangle(self, points: List[List[int]]) -> int:
        """調試版本，包含詳細的執行日誌"""
        
        if len(points) < 2:
            return 0
        
        print(f"處理 {len(points)} 個點")
        
        # 座標壓縮
        x_coords = {}
        y_coords = {}
        
        for x, y in points:
            x_coords[x] = 0
            y_coords[y] = 0
        
        def compress_coordinates(coord_map):
            sorted_coords = sorted(coord_map.keys())
            for i, coord in enumerate(sorted_coords):
                coord_map[coord] = i + 1
        
        compress_coordinates(x_coords)
        compress_coordinates(y_coords)
        
        print(f"座標壓縮: {len(x_coords)} 個不同的x, {len(y_coords)} 個不同的y")
        
        # 建立網格和前綴和
        max_x = len(x_coords) + 1
        max_y = len(y_coords) + 1
        grid = [[0] * max_y for _ in range(max_x)]
        point_to_compressed = {}
        
        for x, y in points:
            compressed_x = x_coords[x]
            compressed_y = y_coords[y]
            grid[compressed_x][compressed_y] = 1
            point_to_compressed[(x, y)] = (compressed_x, compressed_y)
        
        # 前綴和
        prefix_sum = [[0] * max_y for _ in range(max_x)]
        
        for i in range(1, max_x):
            for j in range(1, max_y):
                prefix_sum[i][j] = (
                    prefix_sum[i-1][j] + 
                    prefix_sum[i][j-1] - 
                    prefix_sum[i-1][j-1] + 
                    grid[i][j]
                )
        
        # 排序和枚舉
        points.sort(key=lambda p: (p[0], -p[1]))
        
        count = 0
        n = len(points)
        total_pairs = 0
        
        for i in range(n - 1):
            alice_x, alice_y = points[i]
            
            for j in range(i + 1, n):
                bob_x, bob_y = points[j]
                total_pairs += 1
                
                if alice_x <= bob_x and alice_y >= bob_y:
                    alice_cx, alice_cy = point_to_compressed[(alice_x, alice_y)]
                    bob_cx, bob_cy = point_to_compressed[(bob_x, bob_y)]
                    
                    points_in_rect = (
                        prefix_sum[bob_cx][alice_cy] -
                        prefix_sum[alice_cx - 1][alice_cy] -
                        prefix_sum[bob_cx][bob_cy - 1] +
                        prefix_sum[alice_cx - 1][bob_cy - 1]
                    )
                    
                    if points_in_rect == 2:
                        count += 1
                        if count <= 5:  # 只顯示前幾個結果
                            print(f"  有效配對: Alice({alice_x},{alice_y}) Bob({bob_x},{bob_y})")
        
        print(f"檢查了 {total_pairs} 個點對，找到 {count} 個有效配對")
        
        return count


# 測試和驗證
if __name__ == "__main__":
    import time
    
    print("=== 最優解法：座標壓縮 + 前綴和 ===\n")
    
    sol = Solution()
    sol_debug = SolutionDebug()
    
    # 基本正確性測試
    test_cases = [
        ([[1,1],[2,2],[3,3]], 0),
        ([[6,2],[4,4],[2,6]], 2),
        ([[3,1],[1,3],[1,1]], 2),
        ([[1,2],[3,1]], 1),
        ([[2,5],[128653,-2370425]], 1),  # 之前的失敗案例
    ]
    
    print("正確性驗證:")
    all_correct = True
    for points, expected in test_cases:
        result = sol.numberOfPointsInRectangle(points)
        correct = result == expected
        print(f"  {points} -> {result} (預期: {expected}) {'✅' if correct else '❌'}")
        if not correct:
            all_correct = False
    
    print(f"\n基礎測試 {'通過' if all_correct else '失敗'}!")
    
    if not all_correct:
        print("\n調試模式:")
        # 調試失敗的案例
        for points, expected in test_cases:
            result = sol.numberOfPointsInRectangle(points)
            if result != expected:
                print(f"\n調試案例: {points}")
                sol_debug.numberOfPointsInRectangle(points)
    
    # 性能測試
    print("\n=== 性能測試 ===")
    import random
    random.seed(42)
    
    for n in [100, 500, 1000]:
        # 生成測試數據
        test_points = []
        for _ in range(n):
            x = random.randint(0, n * 2)
            y = random.randint(0, n * 2)
            test_points.append([x, y])
        
        # 去重
        unique_points = list({tuple(p): p for p in test_points}.values())
        test_points = unique_points[:n] if len(unique_points) >= n else unique_points
        actual_n = len(test_points)
        
        print(f"\n測試規模: {actual_n} 個點")
        
        start_time = time.time()
        result = sol.numberOfPointsInRectangle(test_points)
        elapsed = time.time() - start_time
        
        print(f"  結果: {result}")
        print(f"  用時: {elapsed:.4f}s")
        print(f"  性能: {actual_n**2/elapsed/1000:.1f}K ops/sec")
        
        if elapsed < 0.01:
            grade = "🏆 優秀"
        elif elapsed < 0.1:
            grade = "✅ 良好"
        elif elapsed < 1.0:
            grade = "⚠️ 合格"
        else:
            grade = "❌ 需優化"
        
        print(f"  評級: {grade}")
    
    print(f"\n=== 算法特點 ===")
    print("🎯 座標壓縮：處理稀疏座標，避免大矩陣")
    print("⚡ 前綴和矩陣：O(1) 範圍查詢，替代 O(n) 遍歷")
    print("📊 智能排序：確保枚舉順序的正確性")
    print("🔧 空間換時間：O(n²) 空間獲得 O(n²) 時間複雜度")
    print("✅ 理論最優：無需啟發式剪枝，算法本質高效")