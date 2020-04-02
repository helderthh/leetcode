# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/


class Trie:

    def __init__(self, val=""):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.children = []
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for letter in word:
            found = node.get(letter) # search in children
            if not found:
                new_node = Trie(letter)
                node.children.append(new_node)
                node = new_node
            else:
                node = found
                
        node.children.append(Trie())
        
    def get(self, letter):
        for c in self.children:
            if c.val == letter:
                return c
        return None
        
    def _search(self, word: str, should_match: bool) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for letter in word:
            found = node.get(letter)
            if not found:
                return False
            node = found
    
        if not should_match:
            return True
        
        return node.get("") is not None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self._search(word, should_match=True)
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._search(prefix, should_match=False)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

