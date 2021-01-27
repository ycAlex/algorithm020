#就是借助字典快速查找，每一个字符对应一个字典，顺序字符作为key，来进行快速查找
#关键是用特殊字符标记每个单词的结尾
class TrieTree:
	def __init__(self):
		self.tire = {}
        
    def insert(self,word):
        root = self.tire:
        for each in word:
            if each not in self.tire:
                root[each] = {}
            root = root[each]
        
        root['#'] ='#'
    
    def search(self,word):
        root = self.tire
        for each in word:
            if each not in root:
                return False
            root = root[each]
        if '#' not in root:
            return False
        return True
    
    def startwith(self, prefix):
        root = self.tire
        for each in prefix:
            if each not in self.tire:
                return False
            root = root[each]
        return True