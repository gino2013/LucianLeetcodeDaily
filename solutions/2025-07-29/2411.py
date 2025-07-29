"""
You are given a 0-indexed array nums of length n, consisting of non-negative integers. For each index i from 0 to n - 1, you must determine the size of the minimum sized non-empty subarray of nums starting at i (inclusive) that has the maximum possible bitwise OR.

In other words, let Bij be the bitwise OR of the subarray nums[i...j]. You need to find the smallest subarray starting at i, such that bitwise OR of this subarray is equal to max(Bik) where i <= k <= n - 1.
The bitwise OR of an array is the bitwise OR of all the numbers in it.

Return an integer array answer of size n where answer[i] is the length of the minimum sized subarray starting at i with maximum bitwise OR.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,0,2,1,3]
Output: [3,3,2,2,1]
Explanation:
The maximum possible bitwise OR starting at any index is 3. 
- Starting at index 0, the shortest subarray that yields it is [1,0,2].
- Starting at index 1, the shortest subarray that yields the maximum bitwise OR is [0,2,1].
- Starting at index 2, the shortest subarray that yields the maximum bitwise OR is [2,1].
- Starting at index 3, the shortest subarray that yields the maximum bitwise OR is [1,3].
- Starting at index 4, the shortest subarray that yields the maximum bitwise OR is [3].
Therefore, we return [3,3,2,2,1]. 
Example 2:

Input: nums = [1,2]
Output: [2,1]
Explanation:
Starting at index 0, the shortest subarray that yields the maximum bitwise OR is of length 2.
Starting at index 1, the shortest subarray that yields the maximum bitwise OR is of length 1.
Therefore, we return [2,1].
 

Constraints:

n == nums.length
1 <= n <= 10^5
0 <= nums[i] <= 10^9

## Core Concept

The problem asks: **For each starting position i, what's the shortest subarray that achieves the maximum possible bitwise OR?**

## Key Understanding: Bitwise OR Properties

1. **OR only increases or stays the same** - once you OR a bit that's 1, it stays 1
2. **Maximum OR from position i** = OR of ALL elements from i to end of array

## Example 1 Walkthrough: `nums = [1,0,2,1,3]`

Let's trace through each starting position:

**Starting at index 0:**
- Subarray [1]: OR = 1 (binary: 001)
- Subarray [1,0]: OR = 1|0 = 1 (binary: 001) 
- Subarray [1,0,2]: OR = 1|0|2 = 3 (binary: 011)
- Subarray [1,0,2,1]: OR = 3|1 = 3 (binary: 011)
- Subarray [1,0,2,1,3]: OR = 3|3 = 3 (binary: 011)

Maximum possible OR from index 0 = 3
Shortest subarray to achieve OR=3: [1,0,2] (length 3)

**Starting at index 1:**
- Subarray [0]: OR = 0
- Subarray [0,2]: OR = 0|2 = 2 (binary: 010)
- Subarray [0,2,1]: OR = 2|1 = 3 (binary: 011)
- Subarray [0,2,1,3]: OR = 3|3 = 3 (binary: 011)

Maximum possible OR from index 1 = 3
Shortest subarray to achieve OR=3: [0,2,1] (length 3)

**Starting at index 2:**
- Subarray [2]: OR = 2 (binary: 010)
- Subarray [2,1]: OR = 2|1 = 3 (binary: 011)
- Subarray [2,1,3]: OR = 3|3 = 3 (binary: 011)

Maximum possible OR from index 2 = 3
Shortest subarray to achieve OR=3: [2,1] (length 2)

**Starting at index 3:**
- Subarray [1]: OR = 1 (binary: 001)
- Subarray [1,3]: OR = 1|3 = 3 (binary: 011)

Maximum possible OR from index 3 = 3
Shortest subarray to achieve OR=3: [1,3] (length 2)

**Starting at index 4:**
- Subarray [3]: OR = 3 (binary: 011)

Maximum possible OR from index 4 = 3
Shortest subarray to achieve OR=3: [3] (length 1)

**Result: [3,3,2,2,1]**

## Why This Makes Sense

The algorithm works because:
1. From any position i, the maximum possible OR is achieved by taking ALL remaining elements
2. But we want the **shortest** subarray that achieves this maximum
3. We expand the subarray one element at a time until we reach the maximum OR
4. Once we hit the maximum, that's our answer for that starting position

The key insight is that bitwise OR is **monotonic** - it never decreases as you add more elements, so we can stop as soon as we reach the global maximum.
"""

from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        
        # 對於每個bit位置，記錄最後一次出現1的位置
        last_bit_pos = [-1] * 32  # 32位整數
        
        # 從右往左處理每個位置
        for i in range(n - 1, -1, -1):
            # 更新當前數字中為1的bit位置
            for bit in range(32):
                if nums[i] & (1 << bit):
                    last_bit_pos[bit] = i
            
            # 找到最遠的需要包含的位置
            max_reach = i
            for bit in range(32):
                if last_bit_pos[bit] != -1:
                    max_reach = max(max_reach, last_bit_pos[bit])
            
            # 子數組長度 = max_reach - i + 1
            answer[i] = max_reach - i + 1
            
        return answer