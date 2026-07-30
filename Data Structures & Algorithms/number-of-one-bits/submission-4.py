class Solution:
    def hammingWeight(self, n: int) -> int:
        int_lst = []
        while n != 1 and n != 0:
            int_lst.append(str(n % 2))
            n = n // 2
        if n == 1: int_lst.append("1")
        signed_str = "".join(int_lst[::-1])

        count = 0
        for i in signed_str:
            if int(i) & 1:
                count += 1
        return count
