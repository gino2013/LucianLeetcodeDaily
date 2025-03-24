class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # 將會議按開始時間排序
        meetings.sort()
        
        # 用於計算被會議佔用的總天數
        meeting_days_count = 0
        # 當前連續會議區間的開始和結束時間，初始設為-1表示尚未開始
        current_start = current_end = -1
        
        # 遍歷所有會議
        for start, end in meetings:
            # 如果當前會議的開始時間大於上一個會議的結束時間，說明有間隔
            if start > current_end:
                # 如果已經有之前的會議區間，計算其天數
                if current_end != -1:
                    meeting_days_count += current_end - current_start + 1
                # 更新新的會議區間起止時間
                current_start, current_end = start, end
            # 如果會議有重疊，更新結束時間為較晚的那個
            else:
                current_end = max(current_end, end)
        
        # 處理最後一個會議區間的天數
        if current_end != -1:
            meeting_days_count += current_end - current_start + 1
        
        # 返回總天數減去被會議佔用的天數，即空閒天數
        return days - meeting_days_count