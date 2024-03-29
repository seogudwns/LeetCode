class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		ans=0
		prefsum=0
		dic={0:1}

		for num in nums:
			prefsum += num

			if prefsum-k in dic:
				ans += dic[prefsum-k]

			if prefsum not in dic: dic[prefsum] = 1
			else: dic[prefsum] += 1

		return ans