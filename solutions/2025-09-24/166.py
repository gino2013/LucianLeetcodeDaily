class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Handle negative sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        # Work with absolute values
        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        result.append(str(numerator // denominator))
        numerator %= denominator

        if numerator == 0:
            return "".join(result)

        # Fractional part
        result.append(".")
        remainder_map = {}  # remainder -> position in result

        while numerator != 0:
            if numerator in remainder_map:
                # Found repeating part
                index = remainder_map[numerator]
                result.insert(index, "(")
                result.append(")")
                break

            remainder_map[numerator] = len(result)
            numerator *= 10
            result.append(str(numerator // denominator))
            numerator %= denominator

        return "".join(result)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Simple fraction
    result1 = sol.fractionToDecimal(1, 2)
    print(f"Test 1: 1/2 = {result1}")  # Expected: "0.5"

    # Test case 2: Whole number
    result2 = sol.fractionToDecimal(2, 1)
    print(f"Test 2: 2/1 = {result2}")  # Expected: "2"

    # Test case 3: Repeating decimal
    result3 = sol.fractionToDecimal(4, 333)
    print(f"Test 3: 4/333 = {result3}")  # Expected: "0.(012)"

    # Test case 4: Zero numerator
    result4 = sol.fractionToDecimal(0, 5)
    print(f"Test 4: 0/5 = {result4}")  # Expected: "0"

    # Test case 5: Negative result
    result5 = sol.fractionToDecimal(-1, 2)
    print(f"Test 5: -1/2 = {result5}")  # Expected: "-0.5"

    # Test case 6: Negative denominator
    result6 = sol.fractionToDecimal(1, -2)
    print(f"Test 6: 1/-2 = {result6}")  # Expected: "-0.5"

    # Test case 7: Both negative
    result7 = sol.fractionToDecimal(-1, -2)
    print(f"Test 7: -1/-2 = {result7}")  # Expected: "0.5"

    # Test case 8: Long repeating cycle
    result8 = sol.fractionToDecimal(1, 3)
    print(f"Test 8: 1/3 = {result8}")  # Expected: "0.(3)"

    # Test case 9: No fractional part
    result9 = sol.fractionToDecimal(10, 1)
    print(f"Test 9: 10/1 = {result9}")  # Expected: "10"
