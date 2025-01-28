class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedword = []

        pointer1 = 0
        pointer2 = 0
        tracker = 0

        while pointer1 < len(word1) or pointer2 < len(word2):
            if pointer1 < len(word1):
                mergedword.append(word1[pointer1])
                pointer1 += 1

            if pointer2 < len(word2):
                mergedword.append(word2[pointer2])
                pointer2 += 1

        return "".join(mergedword)
