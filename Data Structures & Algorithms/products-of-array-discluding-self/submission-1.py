class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = Counter(nums)[0] 
        if count > 1:
            return [0] * len(nums)

        temp = 1
        for x in nums:
            temp *= x if x != 0 else 1
        res = []

        for x in nums:
            if x == 0:
                res.append(temp)
            elif count > 0:
                res.append(0)
            else:
                res.append(temp // x)
        return res