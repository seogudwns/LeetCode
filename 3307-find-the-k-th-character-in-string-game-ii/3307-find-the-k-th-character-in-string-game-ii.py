class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        chk = [int(i) for i in bin(k-1)[2:]]
        curr,cnt,n,m = 0,0,len(operations),26 
        while chk:
            curr = (curr+operations[cnt]*chk.pop())%m
            cnt = (cnt+1)%n

        return chr(97+curr)

# curr == 1: if x == "i" & x.idx == n ( where 2<=2**m<2**(m+1) ) --> par_x = "h" & par_x.idx == n-2**m
# curr == 0: if x == "i" & x.idx == n ( where 2<=2**m<2**(m+1) ) --> par_x = "i" & par_x.idx == n-2**m


# 31 : ( 31 ; 15 7 3 1 ) 1 1 1 1 0
# 28 : ( 28 ; 12 4 2 1 ) 1 1 0 1 1
# 32 : ( 32 ; 16 8 4 2 1 ) 1 1 1 1 1
# 11 : ( 11 ; 3 1 ) 0 0 1 1