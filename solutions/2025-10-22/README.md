# LeetCode 3347: Maximum Frequency of an Element After Performing Operations II

**Difficulty**: Hard
**Topics**: Array, Hash Table, Greedy, Counting

## Problem Description

You are given an integer array `nums` and two integers `k` and `numOperations`.

You must perform an operation `numOperations` times on `nums`, where in each operation you:
- Select an index `i` that was not selected in any previous operations
- Add an integer in the range `[-k, k]` to `nums[i]`

Return the maximum possible frequency of any element in `nums` after performing the operations.

## Examples

### Example 1:
```
Input: nums = [1,4,5], k = 1, numOperations = 2
Output: 2
Explanation:
- Add 0 to nums[1], after which nums becomes [1, 4, 5]
- Add -1 to nums[2], after which nums becomes [1, 4, 4]
```

### Example 2:
```
Input: nums = [5,11,20,20], k = 5, numOperations = 1
Output: 2
Explanation:
- Add 0 to nums[1]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= k <= 10^9`
- `0 <= numOperations <= nums.length`

## Approach

### Key Insight
For any target value `t`, an element `nums[i]` can be transformed to `t` if and only if `|nums[i] - t| <= k`.

### Strategy
1. **Identify Potential Targets**: We only need to consider values that elements can actually reach:
   - Original values in `nums`
   - Boundary values: `nums[i] - k` and `nums[i] + k` for each element

2. **For Each Target Value**:
   - Count elements already at the target (no operation needed)
   - Count elements that can reach the target (needs one operation)
   - Maximum frequency = `already_at_target + min(can_reach_target, numOperations)`

3. **Return Maximum**: The answer is the maximum frequency across all potential targets.

### Why This Works
- Elements already at the target don't need operations
- We can use our available operations to transform nearby elements
- We're limited by either the number of elements that can reach the target, or the number of operations available

## Complexity Analysis

- **Time Complexity**: O(n²) where n is the length of `nums`
  - O(n) to generate potential targets
  - For each target (O(n) targets), we check all elements (O(n))

- **Space Complexity**: O(n)
  - Storage for potential targets set
  - Storage for frequency counter

## Example Walkthrough

### Example 1: `nums = [1,4,5], k = 1, numOperations = 2`

Potential targets: `{0, 1, 2, 3, 4, 5, 6}`

For target = 4:
- Already at target: 1 element (4)
- Can reach target: 2 elements (5 can become 4, 1 cannot reach 4)
- Frequency: 1 + min(2, 2) = 2 ❌ (wait, let me recalculate)

Actually for target = 4:
- Already at target: 1 element (nums[1] = 4)
- Can reach: nums[2] = 5 (distance 1 ≤ k=1) ✓
- nums[0] = 1 (distance 3 > k=1) ✗
- Frequency: 1 + min(1, 2) = 2 ✓

For target = 5:
- Already at target: 1 element
- Can reach: nums[1] = 4 (distance 1 ≤ k=1) ✓
- Frequency: 1 + min(1, 2) = 2 ✓

Maximum frequency = 2

## Implementation Notes

The solution uses:
- `Counter` to efficiently count original frequencies
- A `set` to store unique potential targets
- Simple iteration to check which elements can reach each target

## Related Problems

- LeetCode 1838: Frequency of the Most Frequent Element
- LeetCode 1679: Max Number of K-Sum Pairs
