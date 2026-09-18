class PrefixTree:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        current = self.root
        while len(word):
            if word[0] in current.children:
                current = current.children[word[0]]
                word = word[1:]
            else:
                current.children[word[0]] = TrieNode(word[0])
                current = current.children[word[0]]
                word = word[1:]
        current.children["break"] = True

    def search(self, word: str) -> bool:
        current = self.root
        while len(word):
            if word[0] in current.children:
                current = current.children[word[0]]
                word = word[1:]
            else:
                return False
        return "break" in current.children

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        while len(prefix):
            if prefix[0] in current.children:
                current = current.children[prefix[0]]
                prefix = prefix[1:]
            else:
                return False
        return True
        
class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = dict()
        