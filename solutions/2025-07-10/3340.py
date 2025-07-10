from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        size = len(startTime)
        gapsArr, left = [], 0
        for i in range(size):
            gap = startTime[i] - left
            gapsArr.append(gap)
            left = endTime[i]
        gapsArr.append(eventTime - endTime[-1])

        maxGapPrefix = [0] * size
        maxGapSuffix = [0] * size
        maxGapPrefix[0] = gapsArr[0]
        maxGapSuffix[-1] = gapsArr[-1]

        for i in range(1, size):
            maxGapPrefix[i] = max(maxGapPrefix[i-1], gapsArr[i])
        for i in range(size - 2, -1, -1):
            maxGapSuffix[i] = max(maxGapSuffix[i+1], gapsArr[i+1])

        ans = 0
        for i in range(size):
            curr = gapsArr[i] + gapsArr[i+1]
            barSize = endTime[i] - startTime[i]
            isValid = False
            if i - 1 >= 0 and maxGapPrefix[i - 1] >= barSize:
                isValid = True
            if i + 1 < size and maxGapSuffix[i + 1] >= barSize:
                isValid = True
            if isValid:
                curr += barSize
            ans = max(ans, curr)
        return ans
