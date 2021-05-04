class Solution:  # using Stack
    def backspaceCompare(self, s: str, t: str) -> bool:
        string=[]
        for c in s:
            if c!='#':
                string.append(c)
            else:
                try:
                    string.pop()
                except:
                    continue
        s=string
        string=[]
        for c in t:
            if c!='#':
                string.append(c)
            else:
                try:
                    string.pop()
                except:
                    continue  
        t=string
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i]!=t[i]:
                return False
        return True


# Time - O(M+N)
# Space - O(max(M, N))



class Solution: # iteration
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(S):
            skip=0
            for c in reversed(S):
                if c=="#":
                    skip+=1
                elif skip:
                    skip-=1
                else:
                    yield c
        return all( x==y for x, y in itertools.zip_longest(helper(s),helper(t)))
      
      
      
# Time - O(M+N)
# Space - O(1)
