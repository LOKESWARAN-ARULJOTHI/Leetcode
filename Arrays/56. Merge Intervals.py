class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merge=[]
        for i in intervals:
            if not merge or merge[-1][1]<i[0]:
                merge.append(i)
            else:
                merge[-1][1]=max(merge[-1][1],i[1])
        return merge
    
    
    
    
# Time - O(N log N)
# Space - O(N)
