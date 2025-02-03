class Solution:
    def reverseWords(self, s: str) -> str:
        word1 = s.lstrip().rstrip()
        
        list1 = word1.split()
        list2 = []
        for idx in range(len(list1)):
            if list1[(len(list1)-1)-idx] != " ":
                list2.append(list1[(len(list1)-1) - idx])

        return " ".join(list2)
