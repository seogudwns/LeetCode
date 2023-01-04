class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks = Counter(tasks)
        
        res = 0
        for i in tasks:
            if tasks[i] == 1:
                return -1
            a,b = divmod(tasks[i],3)
            res += a if b == 0 else a+1
        
        return res