import sys
sys.path.insert(0, '/Users/cfh00892977/FM/LucianLeetcodeDaily')
from importlib import import_module
Solution = import_module('2092').Solution


def test_example_1():
    sol = Solution()
    n = 6
    meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
    firstPerson = 1
    result = sol.findAllPeople(n, meetings, firstPerson)
    expected = [0, 1, 2, 3, 5]
    assert sorted(result) == sorted(expected), f"Expected {expected}, got {result}"
    print("Example 1 passed!")


def test_example_2():
    sol = Solution()
    n = 4
    meetings = [[3, 1, 3], [1, 2, 2], [0, 3, 3]]
    firstPerson = 3
    result = sol.findAllPeople(n, meetings, firstPerson)
    expected = [0, 1, 3]
    assert sorted(result) == sorted(expected), f"Expected {expected}, got {result}"
    print("Example 2 passed!")


def test_example_3():
    sol = Solution()
    n = 5
    meetings = [[3, 4, 2], [1, 2, 1], [2, 3, 1]]
    firstPerson = 1
    result = sol.findAllPeople(n, meetings, firstPerson)
    expected = [0, 1, 2, 3, 4]
    assert sorted(result) == sorted(expected), f"Expected {expected}, got {result}"
    print("Example 3 passed!")


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    print("All tests passed!")
