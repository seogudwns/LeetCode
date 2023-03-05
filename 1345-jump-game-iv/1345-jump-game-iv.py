# class Solution:
#     def minJumps(self, arr: List[int]) -> int:
#         n = len(arr)
#         ans,check,map1,map2,bef,aft = -1,[False for _ in range(n)],[{i-1,i+1} for i in range(n)],dict(),[0],[]

#         for i in range(n): 
#             if arr[i] not in map2: map2[arr[i]] = set()
#             map2[arr[i]].add(i)
            
#         for i in map2:
#             for j in map2[i]:
#                 map1[j]=map1[j]|map2[i]
        
#         map1[0].discard(-1)
#         map1[n-1].discard(n)
#         for i in range(n): map1[i].discard(i)
#         # print(map1)
#         while not check[-1]:
#             while bef:
#                 x = bef.pop()
#                 if check[x]: continue
#                 check[x] = True
#                 for i in map1[x]:
#                     if check[i]: continue
#                     aft.append(i)
            
#             bef,aft = aft,[]
#             ans += 1
        
#         return ans
    
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N, groups = len(arr), defaultdict(list)

        for i, el in enumerate(arr): 
            groups[el].append(i)

        vis, vis_groups = set(), set()
        
        def bfs(lvl, dist):
            nextLvl = set()
            
            for i in lvl:
                if i in vis: continue
                if i == N-1: return dist
                
                vis.add(i)
                
                if i: nextLvl.add(i-1)
                if i+1 < N: nextLvl.add(i+1)
                
                if not arr[i] in vis_groups:
                    vis_groups.add(arr[i])
                    nextLvl.update(groups[arr[i]])
            
            return bfs(nextLvl, dist + 1)
            
        return bfs(set([0]), 0)