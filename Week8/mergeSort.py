#归并排序，分段，然后每一段都排序，然后再合并
def mergesort(nums,left,right):
    if right<=left:
        return 
    #右移等于 （Left+right)//2
    mid = (left+right)>>1
    
    mergesort(nums,left,mid)
    mergesort(nums,mid+1,right)
    merge(nums,left,mid,right)

def merge(nums,left,mid,right):
    tmp = []
    i = left
    j = mid+1
    
    while i <=mid and j<=right:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
        
    while i <= mid:
        tmp.append(nums[i]
        i += 1
    while j <= right:
        tmp.append(nums[j])
        j += 1
    nums[left:right+1] = tmp
     
            
        