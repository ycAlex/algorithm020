#这道题没什么了！感谢嘟嘟助教哈！帮我明白了这里是如何回溯的
#我后面参考了个更好的模板，也就是我学习笔记里面所说的，其实不一定非要用删除（pop),通过生成上的策略形成回溯

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(sol,nums,used,res):
            if len(sol) ==len(nums):
                res.append(sol[:])
                return 
            for i in range(len(nums)):
                if not used[i]:
                    used[i] =True
                    helper(sol+[nums[i]],nums,used,res)
                    used[i] = False
        
        res =[]
        used = [False]*len(nums)
        helper([],nums,used,res)
        return res 