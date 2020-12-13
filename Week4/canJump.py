class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = 0
        for i in range(len(nums)):
            if steps<i:
                break
            steps = max(steps,nums[i]+i)
        
        if steps>=len(nums)-1:
            return True
        else:
            return False