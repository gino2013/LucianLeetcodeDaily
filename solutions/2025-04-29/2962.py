class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # find the maximum element of nums
        # 把 maximum element 分配大於k的數量到subarray
        # 分配剩餘的元素到subarray
        # 計算 subarray 的數量

        # 1. 找到陣列中的最大值
        max_val = max(nums)

        # 2. 記錄最大值出現的索引位置
        max_indices = []
        for i, num in enumerate(nums):
            if num == max_val:
                max_indices.append(i)

        # 3. 如果最大值出現次數少於 k，直接返回 0
        if len(max_indices) < k:
            return 0

        # 4. 計算符合條件的子陣列數量
        count = 0
        n = len(nums)
        prev_max_idx = -1 # 用於記錄前一個 k 個最大值組的起始位置前一個索引

        # 遍歷 max_indices，i 代表每個「長度為 k 的最大值索引子序列」的起始索引
        # max_indices[i] 到 max_indices[i+k-1] 構成一個包含 k 個最大值的區間
        for i in range(len(max_indices) - k + 1):
            # 當前這個 k 個最大值組的最左邊最大值索引是 max_indices[i]
            # 當前這個 k 個最大值組的最右邊最大值索引是 max_indices[i+k-1]

            # 這個區間的左邊界 (包含 max_indices[i]) 可以從哪裡開始？
            # 它可以從 prev_max_idx + 1 開始，直到 max_indices[i]
            # 例如，如果前一個 k 個組的起始最大值在索引 5，當前組的起始最大值在索引 8
            # 那麼子陣列的起始位置可以從 6, 7, 8 開始，包含索引 8 的最大值
            # 選擇起始位置 l 的數量 = max_indices[i] - (prev_max_idx + 1) + 1
            #                 = max_indices[i] - prev_max_idx
            start_choices = max_indices[i] - prev_max_idx

            # 這個區間的右邊界 (包含 max_indices[i+k-1]) 可以到哪裡結束？
            # 它可以從 max_indices[i+k-1] 開始，直到陣列末尾 n-1
            # 選擇結束位置 r 的數量 = (n - 1) - max_indices[i+k-1] + 1
            #                 = n - max_indices[i+k-1]
            end_choices = n - max_indices[i+k-1]

            # 對於每一個選擇的起始位置和結束位置的組合，都形成一個包含至少這個 k 個最大值的子陣列
            # 這種組合的數量是兩者相乘
            count += start_choices * end_choices

            # 更新 prev_max_idx 為當前這個 k 個最大值組的起始索引，
            # 這樣在計算下一個 k 個最大值組時，就知道左邊的界線在哪裡
            prev_max_idx = max_indices[i]

        return count