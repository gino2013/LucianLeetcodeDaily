class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        # Find maximum number where num^x <= n
        max_num = 1
        while (max_num + 1) ** x <= n:
            max_num += 1
        
        # dp[i][j] = ways to make sum i using numbers 1 to j
        dp = [[0] * (max_num + 1) for _ in range(n + 1)]
        
        # Base case: there's one way to make sum 0 (use no numbers)
        for j in range(max_num + 1):
            dp[0][j] = 1
        
        for j in range(1, max_num + 1):
            power = j ** x
            for i in range(n + 1):
                # Don't use number j
                dp[i][j] = dp[i][j-1]
                
                # Use number j (if possible)
                if i >= power:
                    dp[i][j] = (dp[i][j] + dp[i - power][j-1]) % MOD
        
        return dp[n][max_num]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: n = 10, x = 2
    # Expected: 1 (3^2 + 1^2 = 9 + 1 = 10)
    print(f"Example 1: {sol.numberOfWays(10, 2)}")  # Should be 1
    
    # Example 2: n = 4, x = 1  
    # Expected: 2 (4^1 = 4 or 3^1 + 1^1 = 3 + 1 = 4)
    print(f"Example 2: {sol.numberOfWays(4, 1)}")   # Should be 2