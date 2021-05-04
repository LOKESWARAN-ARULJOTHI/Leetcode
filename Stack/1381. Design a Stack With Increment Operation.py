class CustomStack:

    def __init__(self, maxSize: int):
        self.arr=[]
        self.top=-1
        self.maxSize=maxSize
        
        

    def push(self, x: int) -> None:
        if self.top<self.maxSize-1:
            self.arr.append(x)
            self.top+=1
        
        

    def pop(self) -> int:
        if self.top>-1:
            self.top-=1
            return self.arr.pop()
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i<= self.top:
                self.arr[i]+=val
                
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)



# Time - push,pop - O(1), increment - O(min(k,n))
# Space - O(N)
