class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        par = [0]*n
        par_tmp = [0]*n
        for i in manager: par[i]+=1
        par[manager[headID]] -= 1
        
        leaf = set()
        for i in range(n): 
            if not par[i]:
                leaf.add(i)
        # print(par)
        # print(leaf)
        while leaf:
            child = leaf.pop()
            # print(f'child = {child}')
            if child == headID: continue
            parent = manager[child]
            # print(f'parent = {parent}')
            
            par_tmp[parent] = max(par_tmp[parent],informTime[child])
            par[parent]-=1
            if not par[parent]: 
                leaf.add(parent)
                informTime[parent] += par_tmp[parent]
                
        # print(informTime)
        return informTime[headID]