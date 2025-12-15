from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        """
        Count the number of smooth descent periods in a stock price array.

        A smooth descent period consists of contiguous days where each day's price
        is exactly 1 less than the previous day's price.

        Key insight: For a descent period of length n, the number of subarrays is:
        1 + 2 + 3 + ... + n = n * (n + 1) / 2

        Time Complexity: O(n) where n is the length of prices
        Space Complexity: O(1)

        Example:
        prices = [3,2,1,4]
        - [3]: length 1, contributes 1
        - [2]: extends to [3,2] (length 2), contributes 2 total (3 so far)
        - [1]: extends to [3,2,1] (length 3), contributes 3 total (6 so far)
        - [4]: breaks the chain, length 1, contributes 1 (7 total)
        """
        if not prices:
            return 0

        result = 0
        length = 1  # Current descent period length

        for i in range(len(prices)):
            # Check if current price continues the descent (exactly 1 less than previous)
            if i > 0 and prices[i] == prices[i - 1] - 1:
                length += 1
            else:
                # Start a new descent period
                length = 1

            # Add the number of subarrays ending at current position
            # A descent period of length n contributes n subarrays ending at position i
            result += length

        return result
