class solution:
    def anagrams(self,s,t):
        if len(t)!=len(s):
            return False
        return sorted(s)==sorted(t)
