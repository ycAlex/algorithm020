#其实这道题开始想歪了，想着是用一个数组记录下来然后走每一次再遍历那个数组
#后面看了题解发现，其实只用一个变量就行，因为每走一次只需更新最大值

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