import file
import find

lengthToWords = {
    1: ["I", "A"],
    2: ["Me", "Or"],
}

for i in range(3, 8):
    lengthToWords[i] = file.readWordFile(i)

lengthsList = [
    ["Forever", 3],
    ["Nothing", 3],
    ["I", 3, 3, "Think", "About", "It"],
    ["I", 3, 3, "Every", "Night", 2],
    ["Forever", 6],
    ["Nothing", 6],
    [3, 4, "Every", "Night"],
    [3, 4, "Think", "About"]
]

exempt = file.getExemptStrings()

for lengths in lengthsList:
    sentences = find.getSentencesOfLengths(lengthToWords, exempt, lengths)
    file.writeSentenceFile(lengths, sentences)