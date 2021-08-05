import file 
import find

strings = file.getCrosswordStrings()

for wordLength in range(3, 8):
    words = find.getWordsOfLength(strings, wordLength)
    file.writeWordFile(wordLength, words)
