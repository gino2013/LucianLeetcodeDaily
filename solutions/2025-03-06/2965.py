class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # find a = appears twice
        # find b = missing num
        # input = grid
        # find n = grid of size n*n
        # return ans[a,b]
        n = len(grid)
        count = {}
        for row in grid:
            for num in row:
                count[num] = count.get(num, 0) + 1

        repeated = 0 
        missing = 0

        for i in range(1, n * n + 1):
            if count.get(i, 0) == 2:
                repeated = i
            elif count.get(i, 0) == 0:
                missing = i

        return [repeated, missing]