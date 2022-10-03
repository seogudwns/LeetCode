class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        left_num = numbers[0]
        right_num = numbers[-1]
        while True:
            sums = left_num + right_num
            if sums == target:
                return [left+1,right+1]
            elif sums < target:
                left += 1
                left_num = numbers[left]
            else:
                right -= 1
                right_num = numbers[right]