import file
import find

lengthToWords = {
    1: ["I", "A"],
    2: ["Me", "Or"],
}

for i in range(3, 8):
    lengthToWords[i] = file.readWordFile(i)

lengthsList = [
    [7, 3],
    #[1, 3, 3, 5, 5, 2],
    [7, 6]
    #[3, 4, 5, 5]
]

exempt = file.getExemptStrings()

for lengths in lengthsList:
    sentences = find.getSentencesOfLengths(lengthToWords, exempt, lengths)
    file.writeSentenceFile(lengths, sentences)