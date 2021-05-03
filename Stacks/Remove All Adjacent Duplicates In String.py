class Solution:
    def removeDuplicates(self, S: str) -> str:
        res=[]
        for c in S:
            if res and c==res[-1]:
                res.pop()
                continue
            res.append(c)
        return ''.join(res)




# Time and Space - O(n)
