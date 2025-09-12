class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # Alice wins if there's at least one vowel in the string
        # If no vowels exist, Alice can't make any move (needs odd vowels)
        # If vowels exist, Alice can take the entire string (guaranteed odd count >= 1)
        vowels = set('aeiou')
        
        for char in s:
            if char in vowels:
                return True
        
        return False


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: "leetcoder" -> True (contains vowels: e, e, o, e)
    assert sol.doesAliceWin("leetcoder") == True
    
    # Example 2: "bbcd" -> False (no vowels)
    assert sol.doesAliceWin("bbcd") == False
    
    # Additional test cases
    assert sol.doesAliceWin("a") == True  # Single vowel
    assert sol.doesAliceWin("xyz") == False  # No vowels
    assert sol.doesAliceWin("aeiou") == True  # All vowels
    assert sol.doesAliceWin("bcdfg") == False  # All consonants
    
    print("All test cases passed!")
