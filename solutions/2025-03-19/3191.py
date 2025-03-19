class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0  # 用於記錄操作次數的計數器
        n = len(nums)  # 獲取數組的長度
        
        # 遍歷數組，直到倒數第三個元素
        for i in range(n - 2):
            # 如果當前元素是0，需要執行翻轉操作
            if nums[i] == 0:
                nums[i] ^= 1  # 將當前元素翻轉（0變1，1變0）
                nums[i + 1] ^= 1  # 將下一個元素翻轉
                nums[i + 2] ^= 1  # 將下下個元素翻轉
                count += 1  # 操作次數加1
        
        # 檢查最後兩個元素是否都為1
        # 如果是，返回操作次數；否則返回-1表示無法完成
        return count if (nums[n - 2] == 1 and nums[n - 1] == 1) else -1