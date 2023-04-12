class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        ans = []
        for i in path:
            if not i or i == '.': continue
            elif i == '..': 
                if ans: ans.pop()
            else: ans.append(i)
                
        return '/'+'/'.join(ans) if ans else '/'