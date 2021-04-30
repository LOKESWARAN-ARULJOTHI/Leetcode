def generatePossibleNextMoves(self, s):
    # write your code here
    length=len(s)
    if length<2:
        return s 
    if length==2 and s=='++':
        return ['--']
    solution=[]
    for i in range(length-1):
        if s[i]==s[i+1]=='+':
            solution.append(s[:i]+'--'+s[i+2:])
    return solution

#Complexity:
#Time = O(n)
#Space = O(m) -> solution list that holds other states of the string
