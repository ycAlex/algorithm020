#通过双指针，只有双指针都指向了英文字母才反转
def reverseOnlyLetters(s):
    #tmp-保存所有的大小写英文字母
    tmp = set()
    for i in range(26):
        tmp.add(chr(i+97))
        tmp.add(chr(i+97).upper())
    
    res = list(s)
    left,right = 0, len(res)-1
    #双指针遍历
    while(left<right):
        #如果左指针指向的不是英文字母，左指针移动
        if res[left] not in tmp:
            left+=1
        #同理右指针
        elif res[right] not in tmp:
            right -=1
        #如果都是交换
        else:
            res[left],res[right] = res[right],res[left]
            left+=1
            right-=1
    
    return ''.join(res)

a = "Test1ng-Leet=code-Q!"
print(reverseOnlyLetters(a))