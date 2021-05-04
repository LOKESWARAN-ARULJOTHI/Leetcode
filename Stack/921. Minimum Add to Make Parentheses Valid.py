class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        valid = 0
        stack=[]
        for c in S:
            if c=="(":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    valid+=1
        valid+=len(stack)
        return valid
     
     
     
# Time - O(N)
# Space - O(N)
