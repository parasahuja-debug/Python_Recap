# Problem: Given an array of strings words, 
# find the longest string s in words such that every prefix of s 
# (built one character at a time) also exists in words. 
# If there are multiple longest strings with the same length, 
# return the lexicographically smallest one. If no such string exists, return "".
# Example:
# words = ["w","wo","wor","worl","world"]
# Output: "world"
# -- every prefix w, wo, wor, worl, world is in the list

# words = ["a","banana","app","appl","ap","apply","apple"]
# Output: "apple"
# -- "apply" and "apple" both length 5, but "apple" < "apply" lexicographically
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:#for every word in word lets say apple
            if ch not in node.children:#if word is not in the word dict of tree
                node.children[ch] = TrieNode()#traverse through the root
                #this case is applicable if there are same starting point and 
                #two words exists
            node = node.children[ch]#now the node is child
        node.is_end = True#after the whole word is traced set is_end

def longestWord(words):
    trie = Trie()#tree object
    for w in words:
        trie.insert(w) #tree insert with method calling

    best = ""#best path

    def dfs(node, path):
        nonlocal best
        # path is buildable up to here (guaranteed by caller only descending into is_end nodes)
        if len(path) > len(best) or (len(path) == len(best) and path < best):
            #first condition is understandable but next condition is when
            #you have multiple branches and we have to find lexicographically
            #smaller
            best = path

        for ch in sorted(node.children):          # sorted → lexicographically smaller explored first
            child = node.children[ch]#for every child "node"of tree lexicographically
            if child.is_end:#if first character is also the end, meaning
                #prefix is there in word, call again
                # prune: only continue if this prefix is itself a word
                dfs(child, path + ch)

    dfs(trie.root, "")
    return best#return the path