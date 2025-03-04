class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Greedy solution
        # find the max power 
        power = 0
        while power ** 3 <= n:
            power += 1
        power -= 1

        # Greedy method to solve problem
        remaining = n
        while power >= 0:
            current_power_value = 3**power
            if remaining >= current_power_value:
                remaining -= current_power_value
            power -= 1

        return remaining == 0