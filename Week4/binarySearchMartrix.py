#其实这个二分查找的矩阵还好
#简单明了，先二分查找确定行，然后再在行上面二分查找找目标值

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rl,rr = 0, len(matrix)-1
        cl,cr = 0, len(matrix[0])-1
        #先查找行
        while(rl<=rr):
            mid = (rl+rr)//2
            #确定了行之后
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                #如果这行没有跳出外层循环，因为确定了这行之后，其他的行就不用看了
                rl = rr+1
                #然后开始二分查找这行即可
                while(cl<=cr):
                    mid2 = (cl+cr)//2
                    if matrix[mid][mid2] == target:
                        return True
                    elif matrix[mid][mid2]>target:
                        cr  = mid2-1
                    else:
                        cl = mid2+1 
                   
            elif matrix[mid][-1]<target:
                rl = mid+1

            else:
                rr = mid -1

        return False


#https://leetcode-cn.com/problems/search-a-2d-matrix/solution/74-sou-suo-er-wei-ju-zhen-er-fen-cha-zha-wozg/
