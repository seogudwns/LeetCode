class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # MLE.. 사실 당연.
        nums = []
        for i in range(len(arr)):
            tmp = 0
            for j in range(len(arr[i])):
                num = 2**(ord(arr[i][j])-97)
                if tmp&num:
                    tmp = 0
                    break
                tmp += num
            if tmp:
                nums.append(tmp)
        
        res = 0
        Q = deque(nums)
        nex = set()
        while True:
            while Q:
                x = Q.popleft()

                check = False
                for i in range(len(nums)):
                    if not x&nums[i]:
                        check = True
                        nex.add(x^nums[i])

                if not check:
                    cnt = bin(x).count('1')
                    if res<cnt:
                        res = cnt
            if not nex:
                return res
            
            Q = deque(nex)
            nex = set()