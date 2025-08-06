class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # 計算負數的數量（小於0的數）
        neg_count = self.binary_search(nums, 0) 
        # 計算正數的數量（大於0的數）
        # 總長度減去小於等於1的數量，得到大於0的數量
        pos_count = len(nums) - self.binary_search(nums, 1)
        # 返回負數和正數計數中的最大值
        return max(neg_count, pos_count)

    def binary_search(self, nums, target):
        # 初始化二分搜尋的左右邊界
        left, right = 0, len(nums) - 1
        # result 初始化為陣列長度，表示如果所有元素都大於等於 target 的情況
        result = len(nums)
        
        # 當左邊界小於等於右邊界時繼續搜尋
        while left <= right:
            # 計算中間點，避免溢出可以用 left + (right - left) // 2
            mid = (left + right) // 2
            # 如果中間元素小於目標值
            if nums[mid] < target:
                # 搜尋右半部分
                left = mid + 1
            else:
                # 如果中間元素大於等於目標值
                # 記錄當前位置，因為這可能是最左邊符合條件的位置
                result = mid
                # 搜尋左半部分以尋找更小的位置
                right = mid - 1
        
        # 返回小於 target 的元素數量
        # 如果 target 是 0，返回的是負數的數量
        # 如果 target 是 1，返回的是小於等於 0 的元素數量
        return result