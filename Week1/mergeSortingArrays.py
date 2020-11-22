#尾部交换，三指针来记录位置
#这道题是简单，不确定用pop,append是否符合题意？感觉按照这个解法不是简单的题了，详细题解链接如下
#https://leetcode-cn.com/problems/merge-sorted-array/solution/san-zhi-zhen-cong-wei-bu-kai-shi-jiao-huan-by-alex/
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        inx1 =m-1
        inx2 = n -1
        end = (m+n)-1
        while(inx2>=0 and inx1>=0):
            if nums2[inx2]>=nums1[inx1]:
                nums1[end] = nums2[inx2]
                inx2 -=1
                end -=1
            else:
                nums1[end] = nums1[inx1]
                nums1[inx1] = 0
                end -=1
                inx1-=1
        if inx2>=0:
            for i in range(inx2+1):
                nums1[i] = nums2[i]