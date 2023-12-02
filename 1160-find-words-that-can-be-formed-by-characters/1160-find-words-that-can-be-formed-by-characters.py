class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        self.counts = [0 for _ in range(26)]
        for i in chars: self.counts[ord(i) - 97] += 1

        return sum(len(i) if self.chk(i) else 0 for i in words)

    def chk(self, word):
        c = [0 for _ in range(26)]
        for i in word: c[ord(i)-97]+=1
        return all(c[i]-self.counts[i]<1 for i in range(26))