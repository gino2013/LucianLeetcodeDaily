"""
LeetCode 3347: Maximum Frequency of an Element After Performing Operations II

Problem:
Given an integer array nums and two integers k and numOperations.
You must perform numOperations operations where each operation:
- Selects an index i that was not selected in any previous operations
- Adds an integer in the range [-k, k] to nums[i]

Return the maximum possible frequency of any element after performing the operations.

Approach:
1. For any target value t, an element nums[i] can become t if |nums[i] - t| <= k
2. For each potential target value:
   - Count elements already at target (no operation needed)
   - Count elements that can reach target (needs operation)
   - Max frequency = already_at_target + min(can_reach_target, numOperations)
3. Key insight: We only need to check values that elements can actually reach
   - Original values in nums
   - Boundary values: nums[i] - k and nums[i] + k

Time Complexity: O(n^2) where n is length of nums
Space Complexity: O(n) for storing potential targets
"""

from typing import List
from collections import Counter


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # Get all potential target values
        # A target is worth considering if some element can reach it
        potential_targets = set()

        # Add original values
        for num in nums:
            potential_targets.add(num)
            # Add boundary values that elements can reach
            potential_targets.add(num - k)
            potential_targets.add(num + k)

        # Count original frequencies
        original_count = Counter(nums)

        max_freq = 0

        # Try each potential target
        for target in potential_targets:
            # Count elements already at target
            already_at_target = original_count[target]

            # Count elements that can reach target (but aren't already there)
            can_reach = 0
            for num in nums:
                if num != target and abs(num - target) <= k:
                    can_reach += 1

            # Maximum frequency for this target
            # = elements already there + min(elements we can transform, operations available)
            freq = already_at_target + min(can_reach, numOperations)
            max_freq = max(max_freq, freq)

        return max_freq


def test_solution():
    sol = Solution()

    # Test case 1
    nums1 = [1, 4, 5]
    k1 = 1
    numOperations1 = 2
    result1 = sol.maxFrequency(nums1, k1, numOperations1)
    print(f"Test 1: nums={nums1}, k={k1}, numOperations={numOperations1}")
    print(f"Output: {result1}, Expected: 2")
    assert result1 == 2, f"Test 1 failed: expected 2, got {result1}"

    # Test case 2
    nums2 = [5, 11, 20, 20]
    k2 = 5
    numOperations2 = 1
    result2 = sol.maxFrequency(nums2, k2, numOperations2)
    print(f"\nTest 2: nums={nums2}, k={k2}, numOperations={numOperations2}")
    print(f"Output: {result2}, Expected: 2")
    assert result2 == 2, f"Test 2 failed: expected 2, got {result2}"

    # Test case 3: All elements same
    nums3 = [5, 5, 5]
    k3 = 1
    numOperations3 = 1
    result3 = sol.maxFrequency(nums3, k3, numOperations3)
    print(f"\nTest 3: nums={nums3}, k={k3}, numOperations={numOperations3}")
    print(f"Output: {result3}, Expected: 3")
    assert result3 == 3, f"Test 3 failed: expected 3, got {result3}"

    # Test case 4: No operations
    nums4 = [1, 2, 3, 4, 5]
    k4 = 1
    numOperations4 = 0
    result4 = sol.maxFrequency(nums4, k4, numOperations4)
    print(f"\nTest 4: nums={nums4}, k={k4}, numOperations={numOperations4}")
    print(f"Output: {result4}, Expected: 1")
    assert result4 == 1, f"Test 4 failed: expected 1, got {result4}"

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_solution()
