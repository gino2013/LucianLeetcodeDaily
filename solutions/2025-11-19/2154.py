from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        """
        Keep multiplying original by 2 as long as it exists in nums.

        Approach:
        1. Convert nums to a set for O(1) lookup time
        2. Keep checking if original is in the set
        3. If found, multiply by 2 and continue
        4. If not found, return the current value

        Time Complexity: O(n + k) where n is length of nums, k is number of multiplications
        Space Complexity: O(n) for the set
        """
        num_set = set(nums)

        while original in num_set:
            original *= 2

        return original


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [5, 3, 6, 1, 12]
    original1 = 3
    result1 = sol.findFinalValue(nums1, original1)
    print(f"Example 1: nums = {nums1}, original = {original1}")
    print(f"Output: {result1}")
    print(f"Expected: 24")
    print(f"Pass: {result1 == 24}\n")

    # Example 2
    nums2 = [2, 7, 9]
    original2 = 4
    result2 = sol.findFinalValue(nums2, original2)
    print(f"Example 2: nums = {nums2}, original = {original2}")
    print(f"Output: {result2}")
    print(f"Expected: 4")
    print(f"Pass: {result2 == 4}\n")

    # Additional test case: single element
    nums3 = [8]
    original3 = 8
    result3 = sol.findFinalValue(nums3, original3)
    print(f"Example 3: nums = {nums3}, original = {original3}")
    print(f"Output: {result3}")
    print(f"Expected: 16")
    print(f"Pass: {result3 == 16}\n")
