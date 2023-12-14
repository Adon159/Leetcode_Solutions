class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        if len(word1) == len(word2):
            for chr in range(0, len(word1)):
                word3 += word1[chr]
                word3 += word2[chr]
            return word3

        elif len(word1) > len(word2):
            for chr in range(0, len(word2)):
                word3 += word1[chr]
                word3 += word2[chr]
            word3 += word1[len(word2):]
            return word3

        elif len(word2) > len(word1):
            for chr in range(0, len(word1)):
                word3 += word1[chr]
                word3 += word2[chr]
            word3 += word2[len(word1):]
            return word3

