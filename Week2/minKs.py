#不觉得面试会问这么简单的，如果问了，这样写没啥问题吧？毕竟觉得调包是个人都会。。。
#提交这个主要是为了前k个高频做个引子，因为两题类似都是通过堆来得到k大的

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        return heapq.nsmallest(k, arr)
        #return sorted(arr)[:k]