from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Doubly linked list: prev[i] is index of previous element, -1 if none
        # nxt[i] is index of next element, -1 if none
        prev = [i - 1 for i in range(n)]
        nxt = [i + 1 if i + 1 < n else -1 for i in range(n)]
        vals = nums[:]
        removed = [False] * n

        # Count decreasing pairs (where nums[i] > nums[i+1])
        dec_count = sum(1 for i in range(n - 1) if nums[i] > nums[i + 1])

        if dec_count == 0:
            return 0

        # Min-heap: (sum, left_idx, right_idx)
        # Ties broken by left_idx (leftmost pair wins)
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i, i + 1))

        operations = 0

        while dec_count > 0:
            # Find valid minimum pair (lazy deletion)
            while heap:
                s, l, r = heapq.heappop(heap)
                # Check if this pair is still valid:
                # - both exist, are adjacent, AND sum is still correct
                if not removed[l] and not removed[r] and nxt[l] == r and vals[l] + vals[r] == s:
                    break
            else:
                break

            operations += 1

            pl = prev[l]  # previous of left
            nr = nxt[r]   # next of right

            # Remove old contributions to dec_count
            if pl != -1 and vals[pl] > vals[l]:
                dec_count -= 1
            if vals[l] > vals[r]:
                dec_count -= 1
            if nr != -1 and vals[r] > vals[nr]:
                dec_count -= 1

            # Merge: keep l with new value, remove r
            vals[l] = vals[l] + vals[r]
            removed[r] = True
            nxt[l] = nr
            if nr != -1:
                prev[nr] = l

            # Add new contributions to dec_count
            if pl != -1 and vals[pl] > vals[l]:
                dec_count += 1
            if nr != -1 and vals[l] > vals[nr]:
                dec_count += 1

            # Add new pairs to heap
            if pl != -1:
                heapq.heappush(heap, (vals[pl] + vals[l], pl, l))
            if nr != -1:
                heapq.heappush(heap, (vals[l] + vals[nr], l, nr))

        return operations


def test_solution():
    sol = Solution()

    # Test case 1
    nums1 = [5, 2, 3, 1]
    result1 = sol.minimumPairRemoval(nums1)
    print(f"Test 1: {result1} (expected: 2)")
    assert result1 == 2

    # Test case 2
    nums2 = [1, 2, 2]
    result2 = sol.minimumPairRemoval(nums2)
    print(f"Test 2: {result2} (expected: 0)")
    assert result2 == 0

    # Test case 3: single element
    nums3 = [5]
    result3 = sol.minimumPairRemoval(nums3)
    print(f"Test 3: {result3} (expected: 0)")
    assert result3 == 0

    # Test case 4: already sorted
    nums4 = [1, 2, 3, 4, 5]
    result4 = sol.minimumPairRemoval(nums4)
    print(f"Test 4: {result4} (expected: 0)")
    assert result4 == 0

    # Test case 5: reverse sorted - [3,2,1] → merge (2,1)=3 → [3,3] done
    nums5 = [3, 2, 1]
    result5 = sol.minimumPairRemoval(nums5)
    print(f"Test 5: {result5} (expected: 1)")
    assert result5 == 1

    # Test case 6: two elements, decreasing
    nums6 = [2, 1]
    result6 = sol.minimumPairRemoval(nums6)
    print(f"Test 6: {result6} (expected: 1)")
    assert result6 == 1

    # Test case 7: with negative numbers
    nums7 = [1, -3, 2]
    result7 = sol.minimumPairRemoval(nums7)
    print(f"Test 7: {result7} (expected: 1)")  # [1,-3,2] → merge (1,-3)=-2 → [-2,2] done
    assert result7 == 1

    # Test case 8: larger example
    nums8 = [5, 4, 3, 2, 1]
    result8 = sol.minimumPairRemoval(nums8)
    print(f"Test 8: {result8}")  # Multiple merges needed

    print("All tests passed!")

if __name__ == "__main__":
    test_solution()
