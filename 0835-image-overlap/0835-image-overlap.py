'''
[[1,0],[1,0]]
[[0,1],[1,0]]
== 1
'''
# class Solution:
#     def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
#         # return min(sum(sum(img1,[])),sum(sum(img2,[]))) # XX

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_1 = []
        img2_1 = []
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    img1_1.append((i,j))
                if img2[i][j] == 1:
                    img2_1.append((i,j))
        d = {}
        ans = 0
        for a_x, a_y in img1_1:
            for b_x,b_y in  img2_1:
                tr = (b_x - a_x, b_y - a_y)
                if tr in d:
                    d[tr] += 1
                else:
                    d[tr] = 1
                ans = max(ans, d[tr])
        print(d)
        return ans