class Solution:
    def removeStars(self, s: str) -> str:
        star_count = s.count("*")
        for i in range(star_count):
            star_index = s.index("*")
            if star_index == 0:
                s = s[(star_index+1):]
            else:
                s = s[:star_index-1] + s[(star_index+1):]
        return s
