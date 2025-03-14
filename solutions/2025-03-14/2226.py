class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # 1. 確定搜尋範圍
        left, right = 0, max(candies)  # 初始化搜尋範圍：left 為 0（最小可能糖果數），right 為 candies 中的最大值（最大可能糖果數）
        
        # 如果沒有糖果，返回 0
        if sum(candies) == 0:  # 檢查總糖果數是否為 0，若是則無法分配，直接返回 0
            return 0
        
        # 2. 二分搜尋
        while left <= right:  # 當搜尋範圍不為空時，持續進行二分搜尋
            mid = (left + right) // 2  # 計算中間值：mid 為當前猜測的每個孩子可獲得的糖果數
            
            # 3. 特殊情況處理：mid 為 0 時
            if mid == 0:  # 當 mid 等於 0，進行特殊處理
                # 如果 k <= 總糖果數，則 mid = 1 是可能的
                if k <= sum(candies):  # 若孩子數 k 小於等於總糖果數，表示至少可以給每人 1 個糖果
                    left = 1  # 將 left 更新為 1，繼續搜尋更大的值
                else:  # 若 k 大於總糖果數
                    return 0  # 表示無法滿足 k 個孩子，返回 0
                continue  # 跳過本次迴圈，繼續下一次搜尋
            
            # 4. 檢查 mid 的有效性
            count = 0  # 初始化子堆計數器：用於記錄可以分割成大小為 mid 的子堆的總數
            for candy in candies:  # 遍歷每個糖果堆
                count += candy // mid  # 計算當前糖果堆可以分割成多少個大小為 mid 的子堆，並累加到 count 中
            
            # 5. 更新搜尋範圍
            if count >= k:  # 如果子堆數量足夠（大於等於孩子的數量 k），表示 mid 有效
                left = mid + 1  # 嘗試更大的糖果數量：將 left 更新為 mid + 1，縮小搜尋範圍的下界
            else:  # 如果子堆數量不足（小於孩子的數量 k），表示 mid 太大
                right = mid - 1  # 嘗試更小的糖果數量：將 right 更新為 mid - 1，縮小搜尋範圍的上界
        
        # 6. 返回結果
        return right  # 返回 right，即最後一個有效的 mid 值，也就是每個孩子可以獲得的最大糖果數量

