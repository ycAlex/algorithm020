#广搜的例子，套模板就行，关键是明白一点，每次如何往下进行-也就是如何替换产生新的单词
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st = set(wordList)
        if endWord not in st:
            return 0
        m=len(beginWord)
        lqueue = collections.deque()
        lqueue.append(beginWord)
        visited = set()
        step = 1
        visited.add(beginWord)
        while(lqueue):
            for k in range(len(lqueue)):
                cur = lqueue.popleft()
                if cur ==endWord:
                    return step
                for i in range(m):
                    for j in range(26):
                        tmp = cur[:i]+chr(j+97)+cur[i+1:]
                        if tmp in st and tmp not in visited:
                            lqueue.append(tmp)
                            visited.add(tmp)
            step+=1