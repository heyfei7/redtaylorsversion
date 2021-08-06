import enchant
from ReaderWriter import *

englishDictionary = enchant.Dict("en_US")

class Crossword:
    
    # Read Crossword

    def getCols(self):
        cols = [""] * (len(self.crossword[0]))
        for row in self.crossword:
            for i in range(0, len(row)):
                cols[i] += row[i]
        return cols

    def getDiag(self, i, j):
        def valid(a, b):
            return (0 <= a < self.row_n) and (0 <= b < self.col_n)
    
        i1 = i
        j1 = j
        i2 = i
        j2 = j
        s1 = ""
        s2 = ""

        while valid(i1, j1):
            s1 += self.crossword[i1][j1]
            i1 += 1
            j1 += 1
        
        while valid(i2, j2):
            s2 += self.crossword[i2][j2]
            i2 += 1
            j2 -= 1
        return s1, s2

    def getDiags(self):
        diags = list()
        for i in range(0, self.row_n):
            j = 0
            d1, d2 = self.getDiag(i, j)
            diags.append(d1)
            diags.append(d2)

        for j in range(0, self.col_n):
            i = 0
            d1, d2 = self.getDiag(i, j)
            diags.append(d1)
            diags.append(d2)

        return diags

    # Get Words

    @staticmethod
    def getWordsFromString(string, length):
        words = set()
        for start in range(0, len(string)):
            end = start + length
            if end <= len(string):
                s = string[start:end]
                if len(s) == length:
                    if englishDictionary.check(s):
                        words.add(s)
                    if englishDictionary.check(s[::-1]):
                        words.add(s[::-1])
        return words 

    def getWordsOfLength(self, length):
        words = set()
        for string in self.strings:
            words = words.union(Crossword.getWordsFromString(string, length))
        return words

    # Init
    def __init__(self, filename):
        super().__init__()
        self.crossword = ReaderWriter(filename).read()
        self.row_n = len(self.crossword)
        self.col_n = len(self.crossword[0])
        self.strings = self.crossword + self.getCols() + self.getDiags()
