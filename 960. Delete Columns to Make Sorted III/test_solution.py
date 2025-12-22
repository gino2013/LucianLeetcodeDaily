from solution import Solution


def test_example1():
    """After deleting columns 0, 1, and 4, we get ['bc', 'az']"""
    sol = Solution()
    strs = ["babca", "bbazb"]
    result = sol.minDeletionSize(strs)
    assert result == 3, f"Expected 3, got {result}"
    print("✓ Test example 1 passed")


def test_example2():
    """Single row in descending order needs 4 deletions"""
    sol = Solution()
    strs = ["edcba"]
    result = sol.minDeletionSize(strs)
    assert result == 4, f"Expected 4, got {result}"
    print("✓ Test example 2 passed")


def test_example3():
    """All rows already sorted, no deletions needed"""
    sol = Solution()
    strs = ["ghi", "def", "abc"]
    result = sol.minDeletionSize(strs)
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test example 3 passed")


def test_single_column():
    """Single column always sorted"""
    sol = Solution()
    strs = ["a", "b", "c"]
    result = sol.minDeletionSize(strs)
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test single column passed")


def test_all_same_characters():
    """All same characters, no deletions needed"""
    sol = Solution()
    strs = ["aaa", "aaa"]
    result = sol.minDeletionSize(strs)
    assert result == 0, f"Expected 0, got {result}"
    print("✓ Test all same characters passed")


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_example3()
    test_single_column()
    test_all_same_characters()
    print("\nAll tests passed!")
