class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # return ''.join(word1) == ''.join(word2)
        l,r,currl,currr = 0,0,0,0
        lengl,lengr = len(word1[currl]),len(word2[currr])
        
        while True:
            try:
                if l == lengl:
                    currl += 1
                    lengl = len(word1[currl])
                    l = 0
                if r == lengr:
                    currr += 1
                    lengr = len(word2[currr])
                    r = 0
                    
                # print(word1[currl][l],word2[currr][r])
                if word1[currl][l] != word2[currr][r]:
                    return False

                l += 1
                r += 1
                
            except:
                # print(currl, len(word1), currr, len(word2), r, lengr)
                # print((currl == len(word1) and currr+1 == len(word2) and r == lengr))
                # print(currr == len(word2))
                if (currl == len(word1) and currr+1 == len(word2) and r == lengr):
                    if currr == len(word2):
                        return False
                    return True
                return False