import enchant
from ReaderWriter import *

class WordsBag:
    def __init__(self, wordsDir, shortestWord, longestWord, exemptDir=""):
        super().__init__()
        self.wordsDir = ReaderWriterDir(wordsDir, ".txt")
        self.exemptDir = ReaderWriterDir(exemptDir, ".txt")
        self.exempt = exemptDir != ""
        self.shortestWord = shortestWord
        self.longestWord = longestWord
        self.bag = dict()
        
    def read(self):
        for wordLength in range(self.shortestWord, self.longestWord):
            words = set()
            words = words.union(self.wordsDir.read(wordLength))
            if self.exempt:
                words = words.difference(self.exemptDir.read(wordLength))
            self.bag[wordLength] = words
        return self.bag
    
    def load(self, index, words):
        self.bag[index] = words
        
    def write(self):
        for wordLength, words in self.bag.items():
            self.wordsDir.write(wordLength, words)