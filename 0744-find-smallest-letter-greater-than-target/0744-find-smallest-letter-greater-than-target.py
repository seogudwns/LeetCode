class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        x={ord(i) if ord(i)>ord(target) else 200 for i in letters}
        return chr(min(x)) if x!={200} else letters[0]