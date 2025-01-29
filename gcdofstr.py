class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Greatest Common Divisor of Strings

        len1 = len(str1)
        len2 = len(str2)

        def isDivisor(k):
            if len1 % k or len2 % k:
                return False
            
            fac1 , fac2 = len1 // k , len2 // k

            return str1[:k] * fac1 == str1 and str1[:k] * fac2 == str2
                

        for i in range(min(len1,len2),0,-1):
            if isDivisor(i):
                return str1[:i]
            
        return ""

