#使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
#其实找无序的地方就是找出来最大值或最小值，因为是一半有序数组其实也就是一个拐点
#这里找最大值下标
#这个最大值写了好久，绕了半天最后实在没招加了个Break,现在看过来应该是找到最大和最小之后，Left=mid提不上去了


def find_max_index(nums):
    left,right = 0,len(nums)-1
    while(left<right):
        mid = (left+right)//2
        #如果mid的值都比左侧还小了，则可以肯定右边不可能有最大值了
        if nums[mid]<nums[left]:
            right = mid -1
        #如果中间值大左侧，则表明左边不可能在左侧，但是mid有可能是最大值
        elif nums[mid]>nums[left]:
            left = mid
        #这个break是我试了俩例子反应过来的,说实话没太想明白这个具体该怎么写比较好
        #总觉得加个break不太好
        else: 
           break
    return nums[left]
 
 
a= find_max_index([3,4, 5, 6, 7,10,11,-8,-7, 0, 1, 2])
print(a)