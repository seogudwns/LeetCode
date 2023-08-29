class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curr = customers.count('Y')
        ans,mini = 0,curr
        for i in range(len(customers)):
            if customers[i] == 'Y': curr -= 1
            else: curr += 1
            
            if curr < mini:
                mini,ans = curr,i+1
        
        return ans