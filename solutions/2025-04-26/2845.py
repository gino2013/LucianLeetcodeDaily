class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # 總共的subarray
        total_interesting_subarrays = 0
        # 前綴和 = 符合條件的數量總和
        current_prefix_sum_rem = 0
        # 用一個 dictionary 記錄的是「前綴和對 modulo 取模後的餘數」出現的次數
        remainder_counts = {0: 1}

        for num in nums:
            contribution = 1 if num % modulo == k else 0
            current_prefix_sum_rem = (current_prefix_sum_rem + contribution) % modulo
            target_rem_for_prefix_l = (current_prefix_sum_rem - k + modulo) % modulo
            total_interesting_subarrays += remainder_counts.get(target_rem_for_prefix_l, 0)
            remainder_counts[current_prefix_sum_rem] = remainder_counts.get(current_prefix_sum_rem, 0) + 1

        return total_interesting_subarrays