from typing import List
import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        For each spell, find the number of potions that form a successful pair.
        A pair is successful if spell * potion >= success.

        Approach:
        1. Sort the potions array
        2. For each spell, find the minimum potion strength needed: ceil(success / spell)
        3. Use binary search to find the first potion >= minimum required strength
        4. Count = total potions - index of first valid potion

        Time: O(n*log(m) + m*log(m)) where n = len(spells), m = len(potions)
        Space: O(m) for sorting
        """
        # Sort potions for binary search
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            # Find minimum potion strength needed
            # spell * potion >= success
            # potion >= success / spell
            min_potion = (success + spell - 1) // spell  # This is ceil(success / spell)

            # Binary search for the leftmost position where potion >= min_potion
            idx = bisect.bisect_left(potions, min_potion)

            # Count of valid potions = total potions - index of first valid potion
            count = m - idx
            result.append(count)

        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    spells1 = [5, 1, 3]
    potions1 = [1, 2, 3, 4, 5]
    success1 = 7
    print(f"Input: spells = {spells1}, potions = {potions1}, success = {success1}")
    print(f"Output: {sol.successfulPairs(spells1, potions1, success1)}")
    print(f"Expected: [4, 0, 3]\n")

    # Example 2
    spells2 = [3, 1, 2]
    potions2 = [8, 5, 8]
    success2 = 16
    print(f"Input: spells = {spells2}, potions = {potions2}, success = {success2}")
    print(f"Output: {sol.successfulPairs(spells2, potions2, success2)}")
    print(f"Expected: [2, 0, 2]\n")

    # Edge case: All pairs successful
    spells3 = [10, 10, 10]
    potions3 = [1, 2, 3]
    success3 = 5
    print(f"Input: spells = {spells3}, potions = {potions3}, success = {success3}")
    print(f"Output: {sol.successfulPairs(spells3, potions3, success3)}")
    print(f"Expected: [3, 3, 3]\n")

    # Edge case: No pairs successful
    spells4 = [1, 1, 1]
    potions4 = [1, 2, 3]
    success4 = 100
    print(f"Input: spells = {spells4}, potions = {potions4}, success = {success4}")
    print(f"Output: {sol.successfulPairs(spells4, potions4, success4)}")
    print(f"Expected: [0, 0, 0]\n")
