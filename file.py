def readFile(filename):
    file = open(filename)
    rows = list()
    for row in file:
        if row.endswith("\n"):
            rows.append(row[:-1])
        else:
            rows.append(row)
    file.close()
    return rows

def writeFile(filename, words):
    file = open(filename, "w")
    for word in words:
        file.write(word + "\n")
    file.close()

# Crossword

def getCols(crossword):
    cols = [""] * (len(crossword[0]))
    for row in crossword:
        for i in range(0, len(row)):
            cols[i] += row[i]
    return cols

def getDiag(i, j, crossword):
    row_n = len(crossword)
    col_n = len(crossword[0])

    def valid(a, b):
        return (0 <= a < row_n) and (0 <= b < col_n)
    
    i1 = i
    j1 = j
    i2 = i
    j2 = j
    s1 = ""
    s2 = ""

    while valid(i1, j1):
        s1 += crossword[i1][j1]
        i1 += 1
        j1 += 1
    
    while valid(i2, j2):
        s2 += crossword[i2][j2]
        i2 += 1
        j2 -= 1
    return s1, s2

def getDiags(crossword):
    row_n = len(crossword)
    col_n = len(crossword[0])

    diags = list()
    for i in range(0, row_n):
        j = 0
        d1, d2 = getDiag(i, j, crossword)
        diags.append(d1)
        diags.append(d2)

    for j in range(0, col_n):
        i = 0
        d1, d2 = getDiag(i, j, crossword)
        diags.append(d1)
        diags.append(d2)

    return diags

def getAllStrings(crossword):
    return crossword + getCols(crossword) + getDiags(crossword)

crosswordFile = "text.txt"
exemptFile = "exempt.txt"
stringsFile = "strings.txt"

def getCrosswordStrings():
    crossword = readFile(crosswordFile)
    return getAllStrings(crossword)

def getAllStrings():
    return readFile(stringsFile)

def getExemptStrings():
    return readFile(exemptFile)

# Words

wordsDir = "words/"
def wordFilename(length):
    return wordsDir + str(length) + ".txt"

def readWordFile(length):
    return readFile(wordFilename(length))

def writeWordFile(length, words):
    return writeFile(wordFilename(length), words)

# Sentences

sentencesDir = "sentences/"
def sentenceFilename(lengths):
    return sentencesDir + "-".join([str(x) for x in lengths]) + ".txt"

def readSentenceFile(lengths):
    return readFile(sentenceFilename(lengths))

def writeSentenceFile(lengths, sentences):
    return writeFile(sentenceFilename(lengths), sentences)
