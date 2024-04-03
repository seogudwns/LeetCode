class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rot = [(1,0),(0,1),(-1,0),(0,-1)]
        m,n = len(board),len(board[0])
        leng = len(word)
        if m*n<leng:
            return False
        board_words = Counter(sum(board,[]))
        for i in word:
            if i not in board_words:
                return False

            board_words[i] -= 1
            if board_words[i] == -1:
                return False

        first = word[0]
        def word_check(cc,cr,curr):
            if curr == leng:
                return True
            # print(cc,cr,curr,word[curr])

            for c,r in rot:
                new_c,new_r = cc+c,cr+r
                if 0<=new_c<m and 0<=new_r<n and board[new_c][new_r] == word[curr]:
                    tmp = board[new_c][new_r]
                    board[new_c][new_r] = '.'
                    if word_check(new_c,new_r,curr+1):
                        return True
                    board[new_c][new_r] = tmp

            return False

        for c in range(m):
            for r in range(n):
                if board[c][r] == first:
                    tmp = board[c][r]
                    board[c][r] = '.'
                    if word_check(c,r,1):
                        return True
                    board[c][r] = tmp
        
        return False