class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return min(counter, key=counter.get)