class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])

        # 儲存到達每個房間的最短時間，初始化為無限大
        min_arrival_time = [[inf] * cols for _ in range(rows)]
        min_arrival_time[0][0] = 0  # 起點時間為 0

        # 最小堆（優先佇列），格式為 (當前時間, row, col)
        heap = [(0, 0, 0)]

        # 四個可能的移動方向：上、下、左、右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            curr_time, row, col = heappop(heap)

            # 如果已到達終點，直接回傳時間
            if row == rows - 1 and col == cols - 1:
                return curr_time

            # 只有當前時間是該房間的最短到達時間才繼續擴展
            if curr_time == min_arrival_time[row][col]:
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        # 等待至 moveTime 才能開始移動，再加 1 秒進入新格子
                        wait_time = max(curr_time, moveTime[new_row][new_col]) + 1

                        # 若這次到達時間比目前記錄的還短，更新並加入堆中
                        if wait_time < min_arrival_time[new_row][new_col]:
                            min_arrival_time[new_row][new_col] = wait_time
                            heappush(heap, (wait_time, new_row, new_col))
