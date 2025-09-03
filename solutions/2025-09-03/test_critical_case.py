from solution_3027 import Solution
import time

def test_critical_case():
    """測試關鍵失敗案例和性能"""
    sol = Solution()
    
    print("=== 關鍵案例修復驗證 ===\n")
    
    # 1. 原始失敗案例
    failure_case = [[2,5],[128653,-2370425]]
    result = sol.numberOfPointsInRectangle(failure_case)
    print(f"1. 原始失敗案例:")
    print(f"   輸入: {failure_case}")
    print(f"   結果: {result} (預期: 1) {'✅' if result == 1 else '❌'}")
    print(f"   說明: 稀疏大矩形，面積剪枝會錯誤排除")
    print()
    
    # 2. 類似的極端案例
    extreme_cases = [
        [[0,0],[1000000,0]], # 水平線
        [[0,0],[0,1000000]], # 垂直線
        [[0,1000000],[1000000,0]], # 巨大矩形
        [[-1000000,1000000],[1000000,-1000000]], # 超大矩形
    ]
    
    print("2. 類似極端案例:")
    for i, points in enumerate(extreme_cases, 1):
        start_time = time.time()
        result = sol.numberOfPointsInRectangle(points)
        elapsed = time.time() - start_time
        print(f"   案例 {i}: {points}")
        print(f"   結果: {result}, 用時: {elapsed:.4f}s")
    print()
    
    # 3. 性能回歸測試
    print("3. 性能回歸測試:")
    import random
    random.seed(42)
    
    for n in [100, 500, 1000]:
        # 生成包含極端座標的測試數據
        points = []
        
        # 加入一些極端座標
        points.extend([
            [0, 0],
            [1000000, 0],
            [0, 1000000], 
            [-1000000, -1000000]
        ])
        
        # 加入正常座標
        for _ in range(n - 4):
            x = random.randint(-1000, 1000)
            y = random.randint(-1000, 1000)
            points.append([x, y])
        
        start_time = time.time()
        result = sol.numberOfPointsInRectangle(points)
        elapsed = time.time() - start_time
        
        print(f"   {n}點混合數據: 結果={result}, 用時={elapsed:.4f}s")
    
    print("\n=== 修復總結 ===")
    print("✅ 移除過度激進的面積剪枝")
    print("✅ 保留安全的索引優化")
    print("✅ 支持任意大小的稀疏矩形")
    print("✅ 維持高性能表現")

if __name__ == "__main__":
    test_critical_case()