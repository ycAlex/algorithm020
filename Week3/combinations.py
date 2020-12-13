#其实这道题和全排列，子集一样
#微调终止条件-只有当终止条件达成才会操作，然后就是如何产生递归
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(res,sol,n,k,inx):
            if len(sol)==k:
                res.append(sol)
                return 
            for i in range(inx,n+1):
                helper(res,sol+[i],n,k,i+1)
        res = []
        helper(res,[],n,k,1)
        return res