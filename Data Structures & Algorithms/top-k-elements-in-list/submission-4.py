class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict(Counter(nums))
        result = []
        for i in range(k):
            biggest = max(count, key=count.get)
            result.append(biggest)
            count.pop(biggest, None)
        return result
        