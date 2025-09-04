class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distance1 = abs(x - z)
        distance2 = abs(y - z)
        
        if distance1 < distance2:
            return 1
        elif distance2 < distance1:
            return 2
        else:
            return 0


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: x=2, y=7, z=4 -> 1
    print(sol.findClosest(2, 7, 4))  # Expected: 1
    
    # Example 2: x=2, y=5, z=6 -> 2
    print(sol.findClosest(2, 5, 6))  # Expected: 2
    
    # Example 3: x=1, y=5, z=3 -> 0
    print(sol.findClosest(1, 5, 3))  # Expected: 0
