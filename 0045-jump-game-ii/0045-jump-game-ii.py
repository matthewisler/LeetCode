class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        n = len(nums)

        curr_end = 0
        curr_far = 0

        for i in range(n-1):
            print(f"curr_far: {curr_far}")
            print(f"i+nums[i]: {i+nums[i]}")
            curr_far = max(curr_far, i+nums[i])
        
            if i == curr_end:
                jumps += 1
                curr_end = curr_far
        
        return jumps




