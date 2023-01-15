class Solution:
    def numberOfGoodPaths(self, value: List[int], edges: List[List[int]]) -> int:
        if not edges and value:
            return len(value)
        
        adjList = defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)


        n = len(adjList)
        # union find 
        parent = list(range(n))

        def findAP(curr):  # find the Absolute parent  
            if parent[curr] == curr: 
                return curr
            parent[curr] = findAP(parent[curr])
            return parent[curr]

        subtree = [[val,1] for val in value]  # [maxVal,maxValCount] 

        res = 0
        for curr in sorted(range(n),key=lambda i: value[i]):
            # add nodes from low to high to adj sub-trees
            currAP = findAP(curr)
            for adj in adjList[curr]:
                adjAP = findAP(adj)
                if currAP==adjAP or value[adj] > value[curr] :  
                    #  ignore adj with val>value[curr] because they will be added later.
                    continue
                
                # if curr Sub tree max value is equal to adj Sub tree max value we find one of its path
                # check how many nodes in the subtree have the same val of the curr
                if subtree[currAP][0] == subtree[adjAP][0] : 
                    res += subtree[currAP][1]*subtree[adjAP][1]     
                    # total combinations is the no of paths from given curr node
                    subtree[currAP][1] += subtree[adjAP][1]         
                    # get count of max val in both subtree
                subtree[adjAP] = subtree[currAP][:]                
                # both curr ap and adj ap subtree are same i.e maxVal and maxValCount are same
                parent[adjAP] = currAP    # union currAP to adjAP subtrees
                
        return res + n
