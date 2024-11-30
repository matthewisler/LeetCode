class Solution:
    def jump(self, nums: List[int]) -> int:
        #starting index of potential range
        near = 0
        #ending index of potential range
        far = 0
        #return value
        jump_count = 0

        while far < len(nums) - 1:
            #find the farthest we can go in 1 jump
            farthest = 0
            #loop through all potential jumps
            for i in range(near, far + 1):
                #get the farthest
                farthest = max(farthest, i + nums[i])
            
            #take the jump
            jump_count += 1
            #new starting range is that furthest previous jump
            near = far + 1
            #new ending range is 
            far = farthest
        
        return jump_count