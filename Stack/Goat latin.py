class Solution:
    def toGoatLatin(self, S: str) -> str:
        words=(S.split())
        for i in range(len(words)):
            if words[i][0].lower() in ['a','e','i','o','u']:
                words[i]=words[i]+'ma'+'a'*(i+1)
            else:
                words[i]=words[i][1:]+words[i][0]+'ma'+'a'*(i+1)
        string=' '
        return (string.join(words))


# Time - O(n^2)
# Space - O(n)
