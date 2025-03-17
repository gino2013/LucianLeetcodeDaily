class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # 每找到一個就用binary search去找有沒有另一個
        # 將找到的兩個數都扣掉
        # 如果沒找到直接回傳false
        # 重複至nums等於零, 回傳true
        nums.sort()  # Sort array: O(n log n)
        
        # Continue while we have at least 2 elements
        while len(nums) >= 2:
            target = nums[0]  # Take first element as target
            left, right = 1, len(nums) - 1  # Binary search bounds
            found = False

            # Binary search for matching number
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    found = True
                    nums.pop(mid)    # Remove matched number: O(n)
                    nums.pop(0)      # Remove target number: O(n)
                    break
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            if not found:  # If no pair found, return False
                return False

        return len(nums) == 0  # True if all numbers paired
