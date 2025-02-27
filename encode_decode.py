class Solution:
    def encode(self, s):
        res=""
        for s in strs:
            res+=str(len(s))+'#'+s
        return res
    def decode(self, s):
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
                length=int(s[i:j])
                i=i+1
                j=1+length
                res.append(s[i:j])
                i=j
        return res


