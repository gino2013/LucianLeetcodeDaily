from typing import List
from collections import defaultdict

def debug_failure_case():
    """調試失敗案例"""
    points = [[2,5],[128653,-2370425]]
    print(f"調試案例: {points}")
    print(f"預期結果: 1")
    print()
    
    # 分析這個案例
    alice_x, alice_y = points[0]  # (2, 5)
    bob_x, bob_y = points[1]      # (128653, -2370425)
    
    print(f"Alice位置: ({alice_x}, {alice_y})")
    print(f"Bob位置: ({bob_x}, {bob_y})")
    print()
    
    # 檢查位置約束
    print("=== 位置約束檢查 ===")
    print(f"alice_x <= bob_x: {alice_x} <= {bob_x} = {alice_x <= bob_x}")
    print(f"alice_y >= bob_y: {alice_y} >= {bob_y} = {alice_y >= bob_y}")
    print(f"位置約束滿足: {alice_x <= bob_x and alice_y >= bob_y}")
    print()
    
    if alice_x <= bob_x and alice_y >= bob_y:
        print("✅ Alice可以在左上，Bob可以在右下")
        
        # 檢查是否有其他點在矩形內
        print("\n=== 衝突檢測 ===")
        print(f"矩形範圍: x∈[{alice_x}, {bob_x}], y∈[{bob_y}, {alice_y}]")
        print("檢查其他點...")
        
        has_conflict = False
        for i, (x, y) in enumerate(points):
            if i == 0 or i == 1:  # 跳過Alice和Bob
                continue
            
            if alice_x <= x <= bob_x and bob_y <= y <= alice_y:
                print(f"❌ 衝突點: ({x}, {y})")
                has_conflict = True
        
        if not has_conflict:
            print("✅ 沒有衝突點，這個配對應該有效")
        
        # 計算矩形面積
        rect_area = (bob_x - alice_x + 1) * (alice_y - bob_y + 1)
        print(f"\n矩形面積: {rect_area:,}")
        print(f"點數量: {len(points)}")
        print(f"面積/點數比: {rect_area / len(points):,.1f}")
    else:
        print("❌ Alice不能在左上，Bob不能在右下")
    
    print("\n=== 測試各種算法 ===")
    
    # 1. 純暴力算法（絕對正確）
    def pure_brute_force(points):
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
    
    # 2. 帶面積剪枝的算法
    def with_area_pruning(points, area_factor=3):
        n = len(points)
        count = 0
        
        for i in range(n):
            alice_x, alice_y = points[i]
            
            for j in range(n):
                if i == j:
                    continue
                
                bob_x, bob_y = points[j]
                
                if alice_x <= bob_x and alice_y >= bob_y:
                    # 面積剪枝
                    rect_area = (bob_x - alice_x + 1) * (alice_y - bob_y + 1)
                    if rect_area > n * area_factor:
                        print(f"  剪枝跳過: Alice({alice_x},{alice_y}) Bob({bob_x},{bob_y}), 面積={rect_area}")
                        continue
                    
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
    
    print("1. 純暴力算法:")
    result1 = pure_brute_force(points)
    print(f"   結果: {result1}")
    
    print("\n2. 帶面積剪枝 (factor=3):")
    result2 = with_area_pruning(points, 3)
    print(f"   結果: {result2}")
    
    print("\n3. 帶面積剪枝 (factor=5):")
    result3 = with_area_pruning(points, 5)
    print(f"   結果: {result3}")
    
    print("\n4. 不剪枝:")
    result4 = with_area_pruning(points, float('inf'))
    print(f"   結果: {result4}")

if __name__ == "__main__":
    debug_failure_case()