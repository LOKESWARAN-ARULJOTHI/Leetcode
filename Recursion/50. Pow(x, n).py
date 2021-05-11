class Solution:
    def myPow(self, x: float, n: int) -> float:
        def function(base,exp):
            if exp==0:
                return 1
            if exp%2==1:
                return base*function(base,exp-1)
            else:
                return function(base*base,exp//2)
        f = function(x,abs(n))
        if n<0:
            f=1/f
        return f
      
      
# Algorithm - if n is odd - x*(x*x) ^ n-1/2 else (x*x) ^ n/2
# Time - O(log N)
# Space - O(1)
