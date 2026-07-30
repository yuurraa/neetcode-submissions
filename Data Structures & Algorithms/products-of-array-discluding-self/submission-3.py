class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if Counter(nums)[0] > 1:
            return [0] * len(nums)

        temp = 1
        for x in nums:
            temp *= x if x != 0 else 1
        res = []
        p = 0 in nums
        for x in nums:
            if x == 0:
                res.append(temp)
            elif p:
                res.append(0)
            else:
                res.append(temp // x)
        return res