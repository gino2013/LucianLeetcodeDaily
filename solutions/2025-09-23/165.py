class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')

        max_len = max(len(v1_parts), len(v2_parts))

        for i in range(max_len):
            v1_num = int(v1_parts[i]) if i < len(v1_parts) else 0
            v2_num = int(v2_parts[i]) if i < len(v2_parts) else 0

            if v1_num < v2_num:
                return -1
            elif v1_num > v2_num:
                return 1

        return 0


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.compareVersion("1.2", "1.10") == -1

    # Example 2
    assert sol.compareVersion("1.01", "1.001") == 0

    # Example 3
    assert sol.compareVersion("1.0", "1.0.0.0") == 0

    # Additional test cases
    assert sol.compareVersion("1.0.1", "1") == 1
    assert sol.compareVersion("7.5.2.4", "7.5.3") == -1

    print("All test cases passed!")
