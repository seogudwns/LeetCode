class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l,r,ans = 0,len(people)-1,0
        while l<r:
            if people[r]+people[l]<=limit:
                l += 1
            r -= 1
            ans += 1
        
        return ans+1 if l==r else ans