class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        open_slots = flowerbed.count(0)
        filled_slots = flowerbed.count(1)
        if open_slots/2 < n and filled_slots/2 <= len(flowerbed):
            return False
        return True
        '''
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0) and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
