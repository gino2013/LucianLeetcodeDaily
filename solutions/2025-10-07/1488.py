from typing import List
import heapq

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = []
        full_lakes = {}  # lake -> day it became full
        dry_days = []    # min heap of available dry days

        for i, lake in enumerate(rains):
            if lake > 0:
                # It's raining on this lake
                ans.append(-1)

                if lake in full_lakes:
                    # Lake is already full, need to check if we can dry it
                    # Find a dry day after the lake became full but before today
                    last_full_day = full_lakes[lake]
                    found = False

                    # Look for a dry day we can use
                    temp_days = []
                    while dry_days:
                        dry_day = heapq.heappop(dry_days)
                        if dry_day > last_full_day and dry_day < i:
                            # Use this dry day to dry the lake
                            ans[dry_day] = lake
                            found = True
                            break
                        else:
                            temp_days.append(dry_day)

                    # Put back unused dry days
                    for day in temp_days:
                        heapq.heappush(dry_days, day)

                    if not found:
                        return []  # Impossible to avoid flood

                # Mark this lake as full
                full_lakes[lake] = i

            else:
                # No rain today, we can choose to dry a lake
                ans.append(1)  # Placeholder, will be updated if needed
                heapq.heappush(dry_days, i)

        # Fill remaining dry days with any valid lake (or 1)
        while dry_days:
            dry_day = heapq.heappop(dry_days)
            ans[dry_day] = 1

        return ans


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    rains1 = [1,2,3,4]
    result1 = sol.avoidFlood(rains1)
    print(f"Input: {rains1}")
    print(f"Output: {result1}")
    print(f"Expected: [-1,-1,-1,-1]")
    print()

    # Test case 2
    rains2 = [1,2,0,0,2,1]
    result2 = sol.avoidFlood(rains2)
    print(f"Input: {rains2}")
    print(f"Output: {result2}")
    print(f"Expected: [-1,-1,2,1,-1,-1] or [-1,-1,1,2,-1,-1]")
    print()

    # Test case 3
    rains3 = [1,2,0,1,2]
    result3 = sol.avoidFlood(rains3)
    print(f"Input: {rains3}")
    print(f"Output: {result3}")
    print(f"Expected: []")
    print()
