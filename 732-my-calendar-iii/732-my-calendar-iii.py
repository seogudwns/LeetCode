class MyCalendarThree:
    def __init__(self):
        self.check_lst = dict()
        self.idx = 0
        
    def book(self, start: int, end: int, idx = 1) -> int:
        st_en = (start,end,self.idx)
        self.idx += 1
        self.check_lst[st_en] = []
        
        for i in self.check_lst:
            # print('is? :',i)
            if start<=i[0] and i[0]<end:
                # print('O')
                self.check_lst[i].append(st_en)
            if i not in self.check_lst[st_en]:
                if i[0]<=start and start<i[1]:
                    self.check_lst[st_en].append(i)
                
        # print({i:len(self.check_lst[i]) for i in self.check_lst})
        # print(self.check_lst)
        return max(len(self.check_lst[i]) for i in self.check_lst)
                
#     def __init__(self):
#         self.seg_tree = [None for _ in range(10**9)] 
#         self.maxi = 0

#     def book(self, start: int, end: int, idx = 1) -> int:
#         if start == end:
#             return
#         elif start+1 == end:
#             self.seg_tree[idx] += 1
#             return self.seg_tree[idx]
        
#         mid = (start+end)//2
#         self.seg_tree[idx] = max(book(self,start,mid,2*idx),book(self,mid+1,end,2*idx+1))
        
#         return self.seg_tree[idx]


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)