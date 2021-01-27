#先选取一个数，将所有比这个数字小的移动到左侧，比这个数大的移动到右侧，然后递归直到全都排序好
#注意以下几点:1.终止条件，2.如何移动，3，如何拿到新的标尺
def quickSort(start,end,nums):
    #递归终止条件
    if start>=end:
        return 
    #返回新的标尺的下标
    pi = partition(start,end,nums)
    #以新的标尺的下标分割左右再次调用
    quickSort(start,pi-1,nums)
    quickSort(pi+1,end,nums)
    

def partition(start,end,nums):
    #每次以启示为标尺
    pivot = nums[start]
    #mark就是要移动的下标
    mark = start
 
    #遍历当前范围
    for i in range(start+1,end+1):
        #如果小的话
        if nums[i]<pivot:
            #注意这里mark先+1，先把小的往标尺后面放
            mark+=1
            nums[mark],nums[i] = nums[i],nums[mark]
    #最后根据mark走到的地方，和标尺进行交换
    #这步保证了，左侧都是比标尺小的，右侧都是比标尺大的！
    nums[start], nums[mark] = nums[mark],nums[start]
    
    return mark
    

a = [5,6,10,34,1,3,-2,0,9]
print(0,len(a)-1)
quickSort(0,len(a)-1,a)
print(a)
  