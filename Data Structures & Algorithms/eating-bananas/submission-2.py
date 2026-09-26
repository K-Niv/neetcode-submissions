class Solution:


    def totalTime(self, piles, rate, h):
        
        time = sum(math.ceil(p / rate) for p in piles)

        if time > h:
            return 1

        else:
            return -1

        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        min_time = None

        if len(piles) == h:
            return high

        while low <= high:
            mid = (low + high) // 2

            if self.totalTime(piles,mid, h) > 0:
                low = mid + 1

            else:
                min_time = mid
                high = mid - 1

        
        return min_time