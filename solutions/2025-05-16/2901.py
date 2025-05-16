class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        
        # Helper function to calculate Hamming distance
        def hamming_distance(s1: str, s2: str) -> int:
            if len(s1) != len(s2):
                return float('inf')
            return sum(c1 != c2 for c1, c2 in zip(s1, s2))
        
        # dp[i] stores the length of the longest subsequence ending at index i
        dp = [1] * n  # Initialize with 1 (each index is a subsequence of length 1)
        # prev[i] stores the previous index in the subsequence ending at i
        prev = [-1] * n
        
        # Dynamic programming
        for i in range(1, n):
            for j in range(i):
                if groups[j] != groups[i] and hamming_distance(words[j], words[i]) == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
        
        # Find the end of the longest subsequence
        max_len = max(dp)
        end_idx = dp.index(max_len)
        
        # Reconstruct the subsequence
        result = []
        curr_idx = end_idx
        while curr_idx != -1:
            result.append(words[curr_idx])
            curr_idx = prev[curr_idx]
        
        return result[::-1]  # Reverse to get the correct order