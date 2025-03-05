class Solution:
    def coloredCells(self, n: int) -> int:
        # n = 1
        # colored_cells = 1
        # n = 2 
        # colored_cells = 1 + 2*2
        # n = 3
        # colored_cells = 1 + 2*2+ 8

        # f(n) = a*n^2+b*n+c
        # n = 1, f(n) = 1
        # n = 2, f(n) = 5
        # n = 3, f(n) = 13
        # -> f(n) = 2n^2-n+1 = 2*n*n -2*n + 1
        colored_cells = 2*n*n -2*n + 1
        return colored_cells