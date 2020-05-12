from typing import List


class Solution:

    def replaceConnected(self, image, sr, sc, prevColor, newColor):
        if newColor == prevColor:
            return image
        if -1 < sr < len(image) and -1 < sc < len(image[0]):
            if image[sr][sc] == prevColor:
                image[sr][sc] = newColor
                self.replaceConnected(
                    image, sr-1, sc, prevColor, newColor)  # Top
                self.replaceConnected(
                    image, sr+1, sc, prevColor, newColor)  # Down
                self.replaceConnected(
                    image, sr, sc-1, prevColor, newColor)  # Left
                self.replaceConnected(
                    image, sr, sc+1, prevColor, newColor)  # Right
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        return self.replaceConnected(image, sr, sc, image[sr][sc], newColor)


s = Solution()
print(s.floodFill(image=[[1, 1, 1], [1, 1, 0],
                         [1, 0, 1]], sr=1, sc=1, newColor=2))
print(s.floodFill(image=[[0, 0, 0], [0, 1, 1]], sr=1, sc=1, newColor=1))
