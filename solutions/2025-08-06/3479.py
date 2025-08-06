from typing import List

class Solution:
    def basketsToRemove(self, fruits: List[int], baskets: List[int]) -> int:
        # Track used baskets
        # 記錄已使用的籃子
        used_baskets = [False] * len(baskets)
        unplaced_count = 0
        
        # Iterate through each fruit type
        # 遍歷每種水果
        for fruit_quantity in fruits:
            placed = False
            
            # Find the leftmost available basket with sufficient capacity
            # 從左到右找第一個容量足夠且未使用的籃子
            for i in range(len(baskets)):
                if not used_baskets[i] and baskets[i] >= fruit_quantity:
                    # Place the fruit into this basket
                    # 將水果放入這個籃子
                    used_baskets[i] = True
                    placed = True
                    break
            
            # If no suitable basket found, count as unplaced
            # 如果沒有找到合適的籃子，計數未放置的水果
            if not placed:
                unplaced_count += 1
        
        return unplaced_count