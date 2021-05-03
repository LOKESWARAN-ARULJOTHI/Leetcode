class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        last=target[-1]
        target=set(target)
        for i in range(1,last+1):
            res.append('Push')
            if i not in target:
                res.append('Pop')
        return res




# Time and Space = O(n)
