import file
import find

guessTemplates = file.readGuessTemplates()
exempt = file.readExemptStrings()
lengthToWords = dict()
for i in range(3, 8):
    lengthToWords[i] = file.readWordFile(i)

for index, guesses in guessTemplates.items():
    sentences = list()
    for lengths in guesses:
        sentences += find.getSentencesOfLengths(lengthToWords, exempt, lengths)
    file.writeGuessFile(index, sentences)