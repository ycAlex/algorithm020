#这道题是简单，我试了下每次pop，然后再append，也能过，不确定面试的话写pop，append是否能行
#https://leetcode-cn.com/problems/merge-sorted-array/solution/san-zhi-zhen-cong-wei-bu-kai-shi-jiao-huan-by-alex/
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #定义上面说的one,two,three三个指针
        inx1 =m-1
        inx2 = n -1
        end = (m+n)-1
        #nums2,和nums1都没走完        
        while(inx2>=0 and inx1>=0):
            #交换nums2的尾部和nums1的尾部
            if nums2[inx2]>=nums1[inx1]:
                nums1[end] = nums2[inx2]
                inx2 -=1
                end -=1
            #将nums1的尾部和最后一个零交换
            else:
                nums1[end] = nums1[inx1]
                nums1[inx1] = 0
                end -=1
                inx1-=1
        #如果nums2没走完，则通过inx2我们也知道了nums1的前面几位是零
        if inx2>=0:
            for i in range(inx2+1):
                nums1[i] = nums2[i]

