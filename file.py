def getFilename(dir, name):
    return dir + str(name) + ".txt"

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

def readCrosswordStrings():
    crossword = readFile(crosswordFile)
    return getAllStrings(crossword)

def readExemptStrings():
    return readFile(exemptFile)

# Words

wordsDir = "words/"
def readWordFile(length):
    return readFile(getFilename(wordsDir, length))

def writeWordFile(length, sentences):
    return writeFile(getFilename(wordsDir, length), sentences)

# Guesses

guessDir = "guess/"
guessTemplateFile = "guess/templates.txt"

def readGuessFile(index):
    guesses = readFile(getFilename(guessDir, index))
    return [x.split(" ") for x in guesses]

def writeGuessFile(index, guesses):
    return writeFile(getFilename(guessDir, index), guesses)

def readGuessTemplates():
    rows = readFile(guessTemplateFile)
    guesses = dict()
    for row in rows:
        words = row.split(" ")
        index = int(words[0])
        guesses.setdefault(index, list())
        guesses[index].append([int(x) if x.isdigit() else str(x) for x in words[1:]])
    return guesses