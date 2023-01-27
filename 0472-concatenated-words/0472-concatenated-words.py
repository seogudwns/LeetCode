# Others solution.
class Solution:    
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        result = []
        def dfs(word, wordset):
            if word == "":
                return True
            for i in range(len(word)):
                if word[:i+1] in wordset:
                    if dfs(word[i+1:], wordset):
                        return True
            return False
        for word in words:
            wordset.remove(word)
            if dfs(word, wordset):
                result.append(word)
            wordset.add(word)
        return result

# not clear. whenever..
# class Solution:
#     def XXX(self,word,idx,stt=1,exception=''):
#         if idx:
#             for i in range(stt,self.NN):
#                 if self.nums[i] == len(word):
#                     return
#                 for j in self.D[self.nums[i]]:
#                     if j in word:
#                         if exception == i:
#                             continue
#                         self.ans.append(word)
#                         return
#         else:
#             for i in range(stt,self.NN):
#                 if self.nums[i] == len(word):
#                     return
#                 for j in self.D[self.nums[i]]:
#                     if j in word:
#                         self.XXX(word,1,stt,j)
#                         return
        
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         self.D = defaultdict(set)
#         for i in words:
#             self.D[len(i)].add(i)
#         del self.D[max(self.D)]
#         self.NN,self.nums = len(self.D),sorted(self.D)
#         mini = self.nums[0]
#         self.ans = []
#         for i in words:
#             if len(i) == mini: continue
#             self.XXX(i,0)
        
#         return self.ans