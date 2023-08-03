# class Solution:
#     def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         n,ans,a,mini =len(queries),[],len(nums),min(nums)
#         nums.sort()
#         for i in range(n):
#             x,m = queries[i]
#             curr,tmp = 0,-1
#             while curr<a and nums[curr]<=m:
#                 if tmp<x^nums[curr]: tmp = x^nums[curr]
#                 curr += 1
#             ans.append(tmp)
        
#         return ans
         
class Trie:
    def __init__(self):
        self.root={}
        self.m=0
    
    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node:
                node[ch]={}
            node=node[ch]

    def compare(self,word,x):
        node=self.root
        t=""
        a,b='0','1'
        for ch in word:
            if ch==a and b in node:
                t+=b
                node=node[b]
            elif ch==b and a in node:
                t+=a
                node=node[a]
            else:
                t+=ch
                node=node[ch]
        ans=int(t,2)^x
        return ans

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie=Trie()
        n,l=len(queries),len(nums)
        for i in range(n):
            queries[i].append(i)
            
        queries = sorted(queries,key=lambda x:x[1])
        nums = sorted(nums)
        res,j,m=[0]*n,0,nums[0]
        
        for i in range(n):
            x,y,z=queries[i]
            if m>y:
                res[z]=-1
                continue
            while j<l and nums[j]<=y:
                word="{:032b}".format(nums[j])
                trie.insert(word)
                j+=1
            word="{:032b}".format(x)
            ans=trie.compare(word,x)
            res[z]=ans
            
        return res