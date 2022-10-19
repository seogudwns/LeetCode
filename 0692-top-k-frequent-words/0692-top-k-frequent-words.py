class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        x = Counter(words)
        x = sorted(x,key=lambda y: (-x[y],y))
        print(x)
        return x[:k] if len(x)>=k else x