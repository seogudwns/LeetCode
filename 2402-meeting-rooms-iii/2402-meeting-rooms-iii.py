class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
#         delayed = deque([]) # 딜레이가 일어났을 때 정보를 저장할 deque.
#         ending_time = [] # heapq.. 시간이 끝나는 것을 저장.
#         time_per_room = dict() # ending_time에 따라 방이 사빈 것을 표기.
#         counter = [0 for _ in range(n)] # 미팅룸이 사용된 횟수(미팅당).
#         used = [0 for _ in range(n)] # 미팅이 끝나는 시간.
        
#         for i in range(len(meetings)):
#             if 
        
        
        
#         return counter.index(max(counter))

        ans = [0] * n
        times = [0] * n
        meetings = sorted(meetings)

        for start, end in meetings:
            flag = False
            minind = -1
            val = float('inf')
            for j in range(n):
                if times[j] < val:
                    val = times[j]
                    minind = j
                if times[j] <= start:
                    flag = True
                    ans[j] += 1
                    times[j] = end
                    break
            if not flag:
                ans[minind] += 1
                times[minind] += (end - start)

        return ans.index(max(ans))
