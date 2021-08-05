
def getWords(row, length):
    forward = set()
    backward = set()
    for start in range(0, len(row)):
        end = start + length
        if end <= 13:
            s = row[start:end]
            if len(s) == length:
                forward.add(s)        
                backward.add(s[::-1])
    return forward, backward

def getWordFromRows(rows, wordLength):
    forward = set()
    backward = set()
    for row in rows:
        fwords, bwords = getWords(row, wordLength)
        forward = forward.union(fwords)
        backward = backward.union(bwords)
    return forward, backward

def getWordFromCols(rows, wordLength):
    forward = set()
    backward = set()

    cols = [""] * (len(rows[0]))
    for row in rows:
        for i in range(0, len(row)-1):
            cols[i] += row[i]
    cols = cols[:-1]

    for col in cols:
        fwords, bwords = getWords(col, wordLength)
        forward = forward.union(fwords)
        backward = backward.union(bwords)

    return forward, backward

def getDiags(i, j, row_n, col_n, rows):

    def valid(a, b):
        return (0 <= a < row_n) and (0 <= b < col_n)
    
    i1 = i
    j1 = j
    i2 = i
    j2 = j
    s1 = ""
    s2 = ""

    while valid(i1, j1):
        s1 += rows[i1][j1]
        i1 += 1
        j1 += 1
    
    while valid(i2, j2):
        s2 += rows[i2][j2]
        i2 += 1
        j2 -= 1
    return s1, s2

def getWordFromDiag(rows, wordLength):
    row_n = 13
    col_n = 13
    ds = list()
    for i in range(0, row_n):
        j = 0
        d1, d2 = getDiags(i, j, row_n, col_n, rows)
        ds.append(d1)
        ds.append(d2)

    for j in range(0, col_n):
        i = 0
        d1, d2 = getDiags(i, j, row_n, col_n, rows)
        ds.append(d1)
        ds.append(d2)

    forward = set()
    backward = set()
    for d in ds:
        fwords, bwords = getWords(d, wordLength)
        forward = forward.union(fwords)
        backward = backward.union(bwords)

    return forward, backward


file = open("text.txt")
wordLength = 7

rows = []
for row in file:
    rows.append(row)

def writeWords(words, file):
    for word in words:
        file.write(word + "\n")
    
for wordLength in range(2, 8):
    newfile = open("words/" + str(wordLength) + ".txt", "w")
    
    fwords, bwards = getWordFromRows(rows, wordLength)
    writeWords(fwords, newfile)
    writeWords(bwards, newfile)
    fwords, bwards = getWordFromCols(rows, wordLength)
    writeWords(fwords, newfile)
    writeWords(bwards, newfile)

    fwords, bwards = getWordFromDiag(rows, wordLength)
    writeWords(fwords, newfile)
    writeWords(bwards, newfile)
    
    newfile.close()

file.close()