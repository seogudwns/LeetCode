# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # The list of NestedInteger elements to be flattened
        self.nestedList = nestedList
        
        # The flattened list of integers
        self.flattenedList = []
        
        # Index to keep track of the current position in the flattenedList
        self.currentIndex = 0

        # Recursively flattens the nested list and adds integers to the flattenedList
        def flatten(currentList):
            for item in currentList:
                if item.isInteger():
                    self.flattenedList.append(item.getInteger())
                else:
                    # Recursively flatten nested lists
                    flatten(item.getList())
        
        # Flatten the nestedList during initialization
        flatten(self.nestedList)

    # Returns the next integer in the flattened list
    def next(self) -> int:
        number = self.flattenedList[self.currentIndex]
        self.currentIndex += 1
        return number

    # Checks if there are more integers in the flattened list
    def hasNext(self) -> bool:
        return self.currentIndex < len(self.flattenedList)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())