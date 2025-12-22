from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        Find minimum columns to delete so each row is in lexicographic order.

        Approach: Use DP to find maximum columns we can keep.
        dp[i] = max number of columns we can keep ending at column i

        For each column i, check all previous columns j < i:
        - If for all rows, strs[row][j] <= strs[row][i], we can extend
        - dp[i] = max(dp[j] + 1) for all valid j

        Time: O(m^2 * n) where m = len(strs[0]), n = len(strs)
        Space: O(m)
        """
        n = len(strs)
        m = len(strs[0])

        # dp[i] = maximum number of columns we can keep ending at column i
        dp = [1] * m

        for i in range(m):
            for j in range(i):
                # Check if we can extend from column j to column i
                can_extend = True
                for row in range(n):
                    if strs[row][j] > strs[row][i]:
                        can_extend = False
                        break

                if can_extend:
                    dp[i] = max(dp[i], dp[j] + 1)

        # Maximum number of columns we can keep
        max_keep = max(dp)

        # Minimum number of columns to delete
        return m - max_keep
