"""
3354. Make Array Elements Equal to Zero

You are given an integer array nums.

Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.

After that, you repeat the following process:

If curr is out of the range [0, n - 1], this process ends.
If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
Else if nums[curr] > 0:
Decrement nums[curr] by 1.
Reverse your movement direction (left becomes right and vice versa).
Take a step in your new direction.

A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.

Return the number of possible valid selections.

Example 1:
Input: nums = [1,0,2,0,3]
Output: 2

Example 2:
Input: nums = [2,3,4,0,4,1,0]
Output: 0

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
There is at least one element i where nums[i] == 0.
"""

class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        """
        Simulate the process for each possible starting position and direction.

        Key insights:
        1. We can only start at positions where nums[curr] == 0
        2. For each such position, we can try both left and right directions
        3. We need to simulate the entire process to see if all elements become 0
        """
        def simulate(start_pos: int, direction: int, arr: list[int]) -> bool:
            """
            Simulate the process starting at start_pos with given direction.
            direction: -1 for left, 1 for right
            Returns True if all elements become 0, False otherwise.
            """
            # Make a copy of the array to avoid modifying the original
            nums_copy = arr[:]
            curr = start_pos
            curr_dir = direction

            # To avoid infinite loops, we set a maximum number of steps
            # Since we decrement by 1 each time we hit a non-zero, and max value is 100,
            # and max length is 100, we won't need more than 100*100*2 steps
            max_steps = 20000
            steps = 0

            while steps < max_steps:
                # Check if curr is out of range
                if curr < 0 or curr >= len(nums_copy):
                    # Check if all elements are 0
                    return all(x == 0 for x in nums_copy)

                # If current position is 0, just move
                if nums_copy[curr] == 0:
                    curr += curr_dir
                else:
                    # Decrement, reverse direction, and move
                    nums_copy[curr] -= 1
                    curr_dir = -curr_dir
                    curr += curr_dir

                steps += 1

            # If we hit max steps, it's likely an infinite loop
            return False

        count = 0
        n = len(nums)

        # Find all positions where nums[i] == 0
        for i in range(n):
            if nums[i] == 0:
                # Try starting at position i going left (-1)
                if simulate(i, -1, nums):
                    count += 1

                # Try starting at position i going right (1)
                if simulate(i, 1, nums):
                    count += 1

        return count


def test_solution():
    sol = Solution()

    # Test case 1
    nums1 = [1, 0, 2, 0, 3]
    result1 = sol.countValidSelections(nums1)
    print(f"Test 1: nums = {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: 2")
    print(f"Pass: {result1 == 2}\n")

    # Test case 2
    nums2 = [2, 3, 4, 0, 4, 1, 0]
    result2 = sol.countValidSelections(nums2)
    print(f"Test 2: nums = {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: 0")
    print(f"Pass: {result2 == 0}\n")

    # Additional test case - single zero
    nums3 = [0]
    result3 = sol.countValidSelections(nums3)
    print(f"Test 3: nums = {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: 2")
    print(f"Pass: {result3 == 2}\n")

    # Additional test case - all zeros
    nums4 = [0, 0, 0]
    result4 = sol.countValidSelections(nums4)
    print(f"Test 4: nums = {nums4}")
    print(f"Output: {result4}")
    print(f"Expected: 6 (3 positions * 2 directions)")
    print(f"Pass: {result4 == 6}\n")


if __name__ == "__main__":
    test_solution()
