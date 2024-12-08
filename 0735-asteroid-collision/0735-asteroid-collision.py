class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        results = []
        for asteroid in asteroids:
            while results and asteroid < 0 and 0 < results[-1]:
                if -asteroid > results[-1]:
                    results.pop()
                    continue
                elif -asteroid == results[-1]:
                    results.pop()
                break
            else:
                results.append(asteroid)
        return results