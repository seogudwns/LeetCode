class BrowserHistory:

    def __init__(self, homepage: str):
        self.br = [homepage]
        self.curr = 1

    def visit(self, url: str) -> None:
        if len(self.br)>self.curr: self.br[:] = self.br[:self.curr]
        self.br.append(url)
        self.curr+=1
        # print(f'insert {url} {self.br}')

    def back(self, steps: int) -> str:
        self.curr = max(1,self.curr-steps)
        # print(f'back {self.br} : {self.curr}, {self.br[self.curr-1]}')
        return self.br[self.curr-1]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.br),self.curr+steps)
        # print(f'forward {self.br} : {self.curr}, {self.br[self.curr-1]}')
        return self.br[self.curr-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)