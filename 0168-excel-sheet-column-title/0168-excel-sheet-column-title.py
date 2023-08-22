class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        return chr(65+(columnNumber-1)%26) if columnNumber<27 else self.convertToTitle((columnNumber-1)//26)+chr(65+(columnNumber-1)%26)