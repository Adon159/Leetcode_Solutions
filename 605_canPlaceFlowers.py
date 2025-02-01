class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = n 

        # Special case: Single slot flowerbed
        if len(flowerbed) == 1:
            return n == 0 or (flowerbed[0] == 0 and n <= 1)

        for idx in range(len(flowerbed)):
            if count <= 0:
                return True  

            if flowerbed[idx] == 0 and (idx == 0 or flowerbed[idx - 1] == 0) and (idx == len(flowerbed) - 1 or flowerbed[idx + 1] == 0):
                flowerbed[idx] = 1  
                count -= 1
                if count <= 0: #returning a condition
                    return True  

        return count <= 0  
