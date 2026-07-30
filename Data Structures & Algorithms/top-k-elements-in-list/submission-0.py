class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict(Counter(nums))
        result = []
        for i in range(k):
            result.append(max(count, key=count.get))
            count.pop(max(count, key=count.get), None)
        return result
        