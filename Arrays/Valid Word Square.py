class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        row=len(words)
        col=len(words[0])
        for i in range(row):
            for j in range(col):
                if words[i][j]!=words[j][i]:
                    return False
        return True 
    
    
# Complexity
# Time - O(m*n)
# Space - O(1)
