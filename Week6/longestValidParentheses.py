#通过栈来计算
#核心两点:1.如何初始化栈-在栈里加个-1，这样如果整个s是合理的-‘（）’，这样pop完最后减去-1就是答案
#         2.如何运用栈，通过添加下标！通过下标的计算来获得长度

def longestValidParentheses(s):
    if not s:return 0
    #初始化栈同时加入-1
    ans = 0
    st = [-1]
    #遍历字符串
    for i in range(len(s)):
        #如果是‘(’入栈
        if s[i] =='(':
            st.append(i)
        else:
            #如果是右括号先出栈
            st.pop()
            #如果栈为空再将整个入栈
            #思考‘（）））’，两个连续的右括号，这样再入栈这样后面再减去的其实就是上一个右括号的位置
            if not st:
                st.append(i)
            else:
                #更新最大长度
                ans = max(ans,i-st[-1])
    return ans 
 
a = "(()"
print(longestValidParentheses(a))