class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        from math import sqrt
        prime=[0 for x in range(n+1)]

        for i in range(4,n+1,2):
            prime[i]=1

        for i in range(3,int(sqrt(n))+1,2):
            if prime[i]==0:
                for j in range(i*i,n+1,i):
                    prime[j]=1

        a=0
        for i in range(2,n):
            if prime[i]==0:
                a+=1
        return a
