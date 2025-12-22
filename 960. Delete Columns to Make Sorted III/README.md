# 960. Delete Columns to Make Sorted III

## Problem Description

Given an array of n strings `strs`, all of the same length, we may choose deletion indices and delete all characters in those indices for each string.

After deletions, we want the final array to have every string (row) in lexicographic order. Return the minimum possible number of deletion indices.

**Example 1:**
```
Input: strs = ["babca","bbazb"]
Output: 3
Explanation: After deleting columns 0, 1, and 4, the final array is ["bc", "az"].
Both rows are individually in lexicographic order.
```

**Example 2:**
```
Input: strs = ["edcba"]
Output: 4
Explanation: If we delete less than 4 columns, the only row will not be lexicographically sorted.
```

**Example 3:**
```
Input: strs = ["ghi","def","abc"]
Output: 0
Explanation: All rows are already lexicographically sorted.
```

## Solution Approach

### Key Insight
Instead of finding the minimum columns to delete, we find the **maximum columns we can keep**. Then:
```
answer = total_columns - max_kept_columns
```

### Algorithm: Dynamic Programming

We need to find the longest subsequence of column indices such that for every row, the characters at those indices are in non-decreasing order.

**DP Definition:**
- `dp[i]` = maximum number of columns we can keep ending at column `i`

**Transition:**
For each column `i`, check all previous columns `j < i`:
- If for all rows, `strs[row][j] <= strs[row][i]`, we can extend from `j` to `i`
- `dp[i] = max(dp[j] + 1)` for all valid `j`
- Otherwise, `dp[i] = 1` (start a new sequence)

**Example Walkthrough (Example 1):**
```
strs = ["babca","bbazb"]
Columns: 0:'b,b'  1:'a,b'  2:'b,a'  3:'c,z'  4:'a,b'

dp[0] = 1                    # Keep column 0
dp[1] = 1                    # 'b' > 'a', can't extend from 0
dp[2] = 1                    # Can't extend (b > a in row 1)
dp[3] = 2                    # Can extend from 0,1,2 (max is 2)
dp[4] = 2                    # Can extend from 1

max(dp) = 2
Answer = 5 - 2 = 3 deletions
```

### Complexity Analysis
- **Time:** O(m² × n) where m = length of each string, n = number of strings
  - For each column i (m iterations)
  - Check all previous columns j < i (m iterations)
  - Check all rows (n iterations)
- **Space:** O(m) for the dp array

## Code
See `solution.py` for implementation.

## Testing
Run tests with:
```bash
python3 test_solution.py
```
