#首先不确定面试允不允许这样调库。。。
#要说这道题的话个人感觉需要明白两点：1.什么是异位词（排序之后相同的）2.要用什么数据结构保存比较好
#具体到语言：python字典的Key不能用list要用tuple
#https://leetcode-cn.com/problems/group-anagrams/solution/49-zi-mu-yi-wei-ci-fen-zu-jie-yong-zi-dian-by-alex/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        tmp = {}
        for each in strs:
            k = tuple(sorted(each))
            tmp[k] = tmp.get(k,[])+[each]
        
        return list(tmp.values())