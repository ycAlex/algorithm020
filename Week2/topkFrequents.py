#其实跟着超哥的训练营，最大的收获就是为了面试一定要用到正确的数据结构。。。
#这个和最小K的题意思一样，关键是两点：1.如何合理的保存次数；2.如何已出现次数来构建堆
#其实对python熟练度一般，主要是语法简单刷题方便。。可能还需要熟练python的库，这里先百度了20分钟查看如何将字典已value为标准构建堆。希望超哥后面能多发些运用堆的题目
#https://leetcode-cn.com/problems/top-k-frequent-elements/solution/347-qian-k-ge-gao-pin-yuan-su-jie-yong-da-ding-dui/
class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        tmp = heapq.nlargest(k,dic.items(),lambda x:x[1])
        res = []
        for each in tmp:
            res.append(each[0]) 
        return res