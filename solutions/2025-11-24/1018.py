"""
1018. Binary Prefix Divisible By 5
Medium

Given a binary array nums (0-indexed), we define xi as the number whose binary
representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

Example 1:
Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.

Example 2:
Input: nums = [1,1,1]
Output: [false,false,false]

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
"""

from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """
        Approach: Iterative Binary to Decimal Conversion with Modulo

        Key Insight:
        - We don't need to store the full decimal number (which could be huge for large arrays)
        - We only care if the number is divisible by 5 (i.e., number % 5 == 0)
        - We can use the property: (a * b + c) % m = ((a % m) * b + c) % m

        Algorithm:
        1. Initialize current = 0 (the decimal value of the current prefix)
        2. For each bit in nums:
           - Shift left by 1 (multiply by 2): current = current * 2
           - Add the new bit: current = current + nums[i]
           - Keep only the remainder when divided by 5: current = current % 5
           - Check if current % 5 == 0 and add to result

        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(n) for the result array (O(1) extra space)
        """
        answer = []
        current = 0

        for bit in nums:
            # Build the number iteratively: shift left and add new bit
            # current * 2 is equivalent to left shift in binary
            current = (current * 2 + bit) % 5

            # Check if divisible by 5
            answer.append(current == 0)

        return answer


# Test cases
def test_solution():
    sol = Solution()

    # Example 1
    nums1 = [0, 1, 1]
    assert sol.prefixesDivBy5(nums1) == [True, False, False]
    print(f"Test 1 passed: {nums1} -> {sol.prefixesDivBy5(nums1)}")

    # Example 2
    nums2 = [1, 1, 1]
    assert sol.prefixesDivBy5(nums2) == [False, False, False]
    print(f"Test 2 passed: {nums2} -> {sol.prefixesDivBy5(nums2)}")

    # Additional test case
    nums3 = [1, 0, 1, 0, 0]
    # Binary: 1(1), 10(2), 101(5), 1010(10), 10100(20)
    # Divisible by 5: False, False, True, True, True
    assert sol.prefixesDivBy5(nums3) == [False, False, True, True, True]
    print(f"Test 3 passed: {nums3} -> {sol.prefixesDivBy5(nums3)}")

    # Edge case: single element
    nums4 = [0]
    assert sol.prefixesDivBy5(nums4) == [True]
    print(f"Test 4 passed: {nums4} -> {sol.prefixesDivBy5(nums4)}")

    nums5 = [1]
    assert sol.prefixesDivBy5(nums5) == [False]
    print(f"Test 5 passed: {nums5} -> {sol.prefixesDivBy5(nums5)}")

    print("\nAll tests passed!")


if __name__ == "__main__":
    test_solution()
