import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Import from the problem file
import importlib.util
spec = importlib.util.spec_from_file_location("solution", os.path.join(os.path.dirname(__file__), "933.py"))
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)

RecentCounter = solution_module.RecentCounter

def test_example_1():
    """Test case from the problem example"""
    counter = RecentCounter()

    result1 = counter.ping(1)
    print(f"ping(1): Expected 1, Got {result1}")
    assert result1 == 1, f"Expected 1, but got {result1}"

    result2 = counter.ping(100)
    print(f"ping(100): Expected 2, Got {result2}")
    assert result2 == 2, f"Expected 2, but got {result2}"

    result3 = counter.ping(3001)
    print(f"ping(3001): Expected 3, Got {result3}")
    assert result3 == 3, f"Expected 3, but got {result3}"

    result4 = counter.ping(3002)
    print(f"ping(3002): Expected 3, Got {result4}")
    assert result4 == 3, f"Expected 3, but got {result4}"

    print("✅ Test 1 passed!")

def test_single_ping():
    """Test with a single ping"""
    counter = RecentCounter()

    result = counter.ping(1000)
    print(f"ping(1000): Expected 1, Got {result}")
    assert result == 1, f"Expected 1, but got {result}"

    print("✅ Test 2 passed!")

def test_all_within_window():
    """Test where all pings are within 3000ms window"""
    counter = RecentCounter()

    result1 = counter.ping(1)
    assert result1 == 1

    result2 = counter.ping(100)
    assert result2 == 2

    result3 = counter.ping(500)
    assert result3 == 3

    result4 = counter.ping(1000)
    print(f"All pings within window: Expected 4, Got {result4}")
    assert result4 == 4, f"Expected 4, but got {result4}"

    print("✅ Test 3 passed!")

def test_removing_old_requests():
    """Test that old requests are properly removed"""
    counter = RecentCounter()

    # Add several requests
    counter.ping(1)
    counter.ping(100)
    counter.ping(3000)

    # Range is [500, 3500], should remove 1 and 100, keep 3000 and 3500
    result = counter.ping(3500)
    print(f"After ping(3500): Expected 2, Got {result}")
    assert result == 2, f"Expected 2, but got {result}"

    # Range is [1001, 4001], should keep 3000, 3500, 4001
    result2 = counter.ping(4001)
    print(f"After ping(4001): Expected 3, Got {result2}")
    assert result2 == 3, f"Expected 3, but got {result2}"

    print("✅ Test 4 passed!")

def test_large_gap():
    """Test with a large time gap between pings"""
    counter = RecentCounter()

    counter.ping(1)
    counter.ping(100)

    # Large gap - should only count this ping
    result = counter.ping(10000)
    print(f"After large gap: Expected 1, Got {result}")
    assert result == 1, f"Expected 1, but got {result}"

    print("✅ Test 5 passed!")

def test_edge_of_window():
    """Test pings at the exact edge of the 3000ms window"""
    counter = RecentCounter()

    counter.ping(1)

    # Exactly 3000ms later - should include both
    result = counter.ping(3001)
    print(f"At edge of window: Expected 2, Got {result}")
    assert result == 2, f"Expected 2, but got {result}"

    # One more ms - first ping should be excluded
    result2 = counter.ping(3002)
    print(f"Just outside window: Expected 2, Got {result2}")
    assert result2 == 2, f"Expected 2, but got {result2}"

    print("✅ Test 6 passed!")

if __name__ == "__main__":
    print("Running tests for Problem 933: Number of Recent Calls")
    print("=" * 70)

    test_example_1()
    print()
    test_single_ping()
    print()
    test_all_within_window()
    print()
    test_removing_old_requests()
    print()
    test_large_gap()
    print()
    test_edge_of_window()

    print()
    print("=" * 70)
    print("🎉 All tests passed!")
