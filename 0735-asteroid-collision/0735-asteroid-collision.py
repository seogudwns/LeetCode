class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for i in asteroids:
            if not ans or i>0:
                ans.append(i)
            else:
                if not ans or ans[-1]<0:
                    ans.append(i)
                else:
                    if ans[-1]+i==0:
                        ans.pop()
                        continue
                    elif ans[-1]+i>0:
                        continue
                    else:
                        while ans and ans[-1]>0 and ans[-1]+i<0:
                            ans.pop()
                        
                        if not ans or ans[-1]<0:
                            ans.append(i)
                        elif ans[-1]+i == 0:
                            ans.pop()

        return ans
                        