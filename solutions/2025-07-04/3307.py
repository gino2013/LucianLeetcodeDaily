# LeetCode 3307 - Alice and Bob's String Game
# 题目要求在不直接构造超长字符串的情况下，返回经过一系列操作后第k个字符。
# 操作0: word = word + word
# 操作1: word = word + next(word)（每个字符变成下一个字母，z变a）
# 逆向思考：从最后一步往前推k的位置来源。

from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # k-1 转为0-based索引
        k -= 1
        # 记录字母偏移量
        shift = 0
        # 只需考虑前60位（2^60 > 1e14，足够覆盖k的范围）
        for i in range(min(len(operations), 60)):
            # 检查k的第i位（二进制）是否为1
            if (k >> i) & 1:
                # 若为1，说明第i次操作的后半部分，需累加shift
                shift += operations[i]
        # 计算最终字符
        return chr((shift % 26) + ord('a'))

# 示例用法
if __name__ == "__main__":
    sol = Solution()
    # 示例1
    k = 5
    operations = [0,0,0]
    print(sol.kthCharacter(k, operations))  # 输出: "a"
    # 示例2
    k = 10
    operations = [0,1,0,1]
    print(sol.kthCharacter(k, operations))  # 输出: "z"
