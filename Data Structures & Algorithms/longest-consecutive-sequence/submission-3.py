class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers, longest = set(nums), 0
        for i in numbers:
            if (i - 1) not in numbers:  # is a start
                current, length = i, 1
                while (current + 1) in numbers:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
