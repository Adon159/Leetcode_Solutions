class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        max_num = 0

        for idx in range(0,len(candies)):
            max_num = max(max_num,candies[idx])

        temp = None 

        for idx in  range(0,len(candies)):
            temp = candies[idx] + extraCandies
            if temp >= max_num:
                output.append(True)
            else:
                output.append(False)

        return output
            
