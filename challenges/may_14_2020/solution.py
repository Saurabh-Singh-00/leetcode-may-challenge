class Trie:

    class Node:
        __slots__ = ('char', 'children', 'is_complete_word')

        def __init__(self, char: str):
            self.char = char
            self.children: dict = dict()
            self.is_complete_word: bool = False

        def __str__(self):
            return self.char

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node("*")

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.root
        for char in word:
            if not temp.children.get(char):
                temp.children.update({char: self.Node(char)})
            temp = temp.children.get(char)
        temp.is_complete_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.root
        for char in word:
            if temp.children.get(char):
                temp = temp.children.get(char)
            else:
                return False
        if temp.is_complete_word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.root
        for char in prefix:
            if temp.children.get(char):
                temp = temp.children.get(char)
            else:
                return False
        return True
