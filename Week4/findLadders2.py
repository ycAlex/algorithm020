#这道单词接龙II 受教育了，开始自己剪枝是对每个分枝加一个set()-来看新生成的单词是否出现过
#然后再一个set()来查看每一个分枝是否出现过来判断是否需要产生新分支-因为这里不管顺序-如hit hot lot = hit lot hot
#看了超哥发的这个代码，通过map来实现，还是得灵活运用！！！！
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        print(wordList)
        res = []
        layer  = {}
        layer[beginWord] = [[beginWord]]
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w ==endWord:
                    res.extend(k for k in layer[w])
                    return res
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                for each in layer[w]:
                                    print(neww)
                                    newlayer[neww]+=[each+[neww]]
                                    print(newlayer)
            wordList -= set(newlayer.keys())
            layer = newlayer
            print('******************')
            
        return res