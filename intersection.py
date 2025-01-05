class Solution:
    def numberofElementsInIntersection(self,a, b):
        intersection_set=set(a).intersection(set(b))
        return len(intersection_set)

