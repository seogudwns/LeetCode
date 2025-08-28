class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n,curr = len(grid),[]

        for i in range(2,2*n-1):
            curr.clear()
            get_leng = min(i,2*n-i)
            # print("=======")
            for j in range(get_leng):
                # print(max(n-i,0)+j,max(i-n,0)+j)
                curr.append(grid[max(n-i,0)+j][max(i-n,0)+j])

            curr = sorted(curr,reverse=i<=n)
            for j in range(get_leng):
                grid[max(n-i,0)+j][max(i-n,0)+j] = curr[j]
        
        return grid