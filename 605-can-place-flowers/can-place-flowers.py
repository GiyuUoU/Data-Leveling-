class Solution:
    def canPlaceFlowers(self, flowerbed, n):

        count = 0
        size = len(flowerbed)

        for i in range(size):

            left = (i == 0 or flowerbed[i-1] == 0)
            right = (i == size-1 or flowerbed[i+1] == 0)

            if flowerbed[i] == 0 and left and right:

                flowerbed[i] = 1
                count += 1

        return count >= n