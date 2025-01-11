class Solution:
    def merge(self,intervals):
        if not intervals or len(intervals)<=0:
            return intervals
        intervals.sort(key=lambda x:x[0])
        merged=[intervals[0]]
        for current in intervals[1:]:
            last=merged[-1]
            if current[0]<=last[1]:
                last[1]=max(current[1],last[1])
            else:
                merged.append(current)
        return merged
intervals=[[2,3],[4,2],[1,4]]
solution=Solution()
mergeIntervals=solution.merge(intervals)
print(mergeIntervals)
