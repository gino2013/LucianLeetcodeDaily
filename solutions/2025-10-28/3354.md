# 3354. Make Array Elements Equal to Zero

## Problem Description

Given an integer array `nums`, start at a position where `nums[curr] == 0` and choose a direction (left or right). Follow these rules:
- If `curr` is out of bounds, the process ends
- If `nums[curr] == 0`, move in the current direction
- If `nums[curr] > 0`, decrement it by 1, reverse direction, and move

Count how many valid starting configurations make all elements zero.

## Solution Approach

**Time Complexity:** O(n × m × sum(nums)) where n is the number of zeros, m is array length
**Space Complexity:** O(m) for the array copy

### Algorithm

1. **Find all zero positions**: Iterate through the array to find all positions where `nums[i] == 0`

2. **Simulate each configuration**: For each zero position, try both directions (left and right)

3. **Simulation logic**:
   - Keep a copy of the array to avoid modifying the original
   - Track current position and direction
   - Follow the rules: move if zero, decrement/reverse/move if non-zero
   - Check if we go out of bounds (terminate and check if all zeros)
   - Use a max step limit to avoid infinite loops

4. **Count valid selections**: Increment counter when simulation results in all zeros

### Key Insights

- We must simulate the entire process for each starting configuration
- The process is deterministic - given a start position and direction, the outcome is fixed
- We need to handle edge cases like going out of bounds and potential infinite loops
- Max steps calculation: With max value 100 and max length 100, we set a safe upper bound

### Example Walkthrough

For `nums = [1,0,2,0,3]`:

**Valid Configuration 1: Start at index 3, go left**
```
[1,0,2,0,3] → curr=3, dir=left → move to 2
[1,0,2,0,3] → curr=2, val=2 → decrement, reverse → [1,0,1,0,3]
[1,0,1,0,3] → curr=3, dir=right → move to 4
...continues until all zeros
```

**Valid Configuration 2: Start at index 3, go right**
```
[1,0,2,0,3] → curr=3, dir=right → move to 4
[1,0,2,0,3] → curr=4, val=3 → decrement, reverse → [1,0,2,0,2]
...continues until all zeros
```

## Edge Cases

- Single element array `[0]`: Both directions valid (goes out of bounds immediately)
- All zeros: Every position and direction is valid
- No valid configuration: Returns 0
