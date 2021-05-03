class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for s in ops:
            if s == 'D':
                res.append(res[-1]*2)
            elif s == 'C':
                res.pop()
            elif s == '+':
                res.append(res[-1]+res[-2])
            elif int(s):
                res.append(int(s))
        return sum(res)


# Time and Space = O(n)
