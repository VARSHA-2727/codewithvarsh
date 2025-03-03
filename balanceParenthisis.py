class Solution:
    def isBalanced(self, s):
        while '()' in s or '[]' in s or '{}' in s:
            s.replace('()','')
            s.replace('[]','')
            s.replace('{}','')
        return s==''
