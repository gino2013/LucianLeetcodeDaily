import sys
sys.path.append('.')

from solution_3027 import Solution
import time
import random

def performance_test():
    sol = Solution()
    
    print("=== 超大規模性能測試 ===\n")
    
    # 測試不同規模的性能
    test_sizes = [100, 300, 500, 1000, 1500]
    
    for n in test_sizes:
        print(f"測試規模: {n} 個點")
        
        # 生成混合分布的測試數據
        random.seed(42)
        points = []
        
        # 50% 稀疏分布
        for _ in range(n // 2):
            x = random.randint(0, n * 10)
            y = random.randint(0, n * 10)
            points.append([x, y])
        
        # 50% 聚集分布
        centers = [(n * 2, n * 2), (n * 8, n * 8), (n * 5, n * 1)]
        for _ in range(n - n // 2):
            center = random.choice(centers)
            x = center[0] + random.randint(-n//10, n//10)
            y = center[1] + random.randint(-n//10, n//10)
            points.append([x, y])
        
        # 去重
        unique_points = list({tuple(p): p for p in points}.values())
        test_points = unique_points[:n] if len(unique_points) >= n else unique_points
        actual_n = len(test_points)
        
        print(f"  實際點數: {actual_n}")
        
        # 性能測試
        start_time = time.time()
        try:
            result = sol.numberOfPointsInRectangle(test_points)
            elapsed = time.time() - start_time
            
            print(f"  結果: {result}")
            print(f"  用時: {elapsed:.4f}s")
            
            # 計算性能指標
            ops_per_sec = (actual_n ** 2) / elapsed / 1000
            print(f"  性能: {ops_per_sec:.1f}K ops/sec")
            
            # 性能評級
            if elapsed < 0.1:
                grade = "🏆 優秀"
            elif elapsed < 1.0:
                grade = "✅ 良好"
            elif elapsed < 5.0:
                grade = "⚠️  合格"
            else:
                grade = "❌ 需優化"
            
            print(f"  評級: {grade}")
            
            # 內存效率檢查
            if actual_n <= 200:
                algorithm = "優化暴力"
            else:
                algorithm = "掃描線"
            print(f"  使用算法: {algorithm}")
            
        except Exception as e:
            print(f"  ❌ 錯誤: {e}")
        
        print()

if __name__ == "__main__":
    performance_test()