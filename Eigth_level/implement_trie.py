class TrieNode:
    def __init__(self):
        self.children = {}      # char -> TrieNode #child of root
        self.is_end = False     # marks end of a word 

class Trie:
    def __init__(self):
        self.root = TrieNode() #create tree node

    def insert(self, word: str) -> None:
        node = self.root #create a node
        for ch in word:#trace every character in the word
            if ch not in node.children:#if character not in tree
                node.children[ch] = TrieNode()#create the trie
            node = node.children[ch]#point to next character in the word
        node.is_end = True#once the word is complete mark end as true

    def search(self, word: str) -> bool:
        node = self.root#create a node
        for ch in word:
            if ch not in node.children[ch]:
                return False
            node=node.children[ch]
        return node.is_end #word exists if node.is_end true
    
        # self._traverse(word)
        # return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for ch in prefix:
            if ch not in node.children[ch]:
                return False
            node=node.children[ch]
        return True #prefix exists
        #        return self._traverse(prefix) is not None

    # def _traverse(self, s: str):
    #     node = self.root
    #     for ch in s:
    #         if ch not in node.children:
    #             return None
    #         node = node.children[ch]
    #     return node