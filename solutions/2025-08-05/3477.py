from typing import List

class Solution:
    def basketsToRemove(self, fruits: List[int], baskets: List[int]) -> int:
        # 記錄已使用的籃子 / Track used baskets
        used_baskets = [False] * len(baskets)
        unplaced_count = 0
        
        # 遍歷每種水果 / Iterate through each fruit type
        for fruit_quantity in fruits:
            placed = False
            
            # 從左到右找第一個容量足夠且未使用的籃子 / Find the leftmost available basket with sufficient capacity
            for i in range(len(baskets)):
                if not used_baskets[i] and baskets[i] >= fruit_quantity:
                    # 將水果放入這個籃子 / Place the fruit into this basket
                    used_baskets[i] = True
                    placed = True
                    break
            
            # 如果沒有找到合適的籃子，計數未放置的水果 / If no suitable basket found, count as unplaced
            if not placed:
                unplaced_count += 1
        
        return unplaced_count