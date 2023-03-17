class Trie:

    def __init__(self):
        self.check = False
        self.child = dict()

    def insert(self, word: str) -> None:
        if not word:
            self.check = True
            return
        nex,w = Trie(),word[0]
        nex.insert(word[1:])
        if w not in self.child: self.child[w] = []
        self.child[w].append(nex)
        
    def search(self, word: str) -> bool:
        if not word:
            return self.check
        w = word[0]
        if w not in self.child: return False
        return any(i.search(word[1:]) for i in self.child[w])

    def startsWith(self, prefix: str) -> bool:
        if not prefix: return True
        
        w = prefix[0]
        if w not in self.child: return False
        return any(i.startsWith(prefix[1:]) for i in self.child[w])

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)