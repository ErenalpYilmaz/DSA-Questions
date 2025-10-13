class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []

        for candy in candies:
            #result.append(candy + extraCandies >= max_candies)
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result