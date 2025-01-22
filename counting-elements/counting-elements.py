class Solution:
    def countElements(self, arr: List[int]) -> int:
        ans = 0
        dic = {}
        for num in arr:
            if num in dic:
                continue
            dic[num] = arr.count(num)
        
        for num in arr:
            if num in dic and num+1 in dic:
                ans += 1
            
        return ans
            