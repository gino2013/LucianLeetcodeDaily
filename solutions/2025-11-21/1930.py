from typing import List

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Count unique palindromic subsequences of length 3.

        For a length-3 palindrome, first and last chars must match.
        For each character that appears at least twice:
        - Find first and last occurrence
        - Count unique characters between them
        - Each unique middle character forms a distinct palindrome
        """
        result = 0

        # Check each character a-z
        for char in 'abcdefghijklmnopqrstuvwxyz':
            # Find first and last occurrence
            first = s.find(char)
            last = s.rfind(char)

            # If character appears at least twice
            if first != -1 and first < last:
                # Count unique characters between first and last occurrence
                # Each unique character between them forms a palindrome: char + middle + char
                middle_chars = set(s[first + 1:last])
                result += len(middle_chars)

        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    s1 = "aabca"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {sol.countPalindromicSubsequence(s1)}")
    print(f"Expected: 3")
    print()

    # Test case 2
    s2 = "adc"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {sol.countPalindromicSubsequence(s2)}")
    print(f"Expected: 0")
    print()

    # Test case 3
    s3 = "bbcbaba"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {sol.countPalindromicSubsequence(s3)}")
    print(f"Expected: 4")
    print()
