class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        lenght = len(flowerbed)

        for i in range(lenght):
            if flowerbed[i] == 0:
                empty_left = (i == 0 or flowerbed[i-1] == 0)
                empty_right = (i == lenght - 1 or flowerbed[i+1] == 0 )

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
        return count >= n