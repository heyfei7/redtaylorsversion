from Crossword import *
from WordsBag import * 
from GuessMaker import *
from ReaderWriter import ReaderWriter

wordsDir = "words/"
exemptDir = "words/exempt/"
guessDir = "guess/"
crosswordFile = "crossword.txt"
templatesFile = "templates.txt"
shortestWord = 1
longestWord = 10
guessIndices = [2, 5, 6, 8]

STEP = 3

# Find Words
if STEP == 1:
    crossword = Crossword(crosswordFile)
    wordsBag = WordsBag(wordsDir, shortestWord, longestWord, exemptDir)

    # (Optional) Get strings and write to file
    ReaderWriter("strings.txt").write(crossword.strings)

    # Get words from crossword
    for wordLength in range(shortestWord, longestWord):
        # get words of length wordLength
        words = crossword.getWordsOfLength(wordLength)
        wordsBag.load(wordLength, words)

    # Write words to file
    wordsBag.write()

    # (Optional) Add words to words/exempt/*.exempt files
    # Words in these files won't be used to construct guesses

# Make Guesses
if STEP == 2:
    # Load templates
    guessTemplates = readGuessTemplate(templatesFile)
    guessMaker = GuessMaker(guessDir, guessIndices)
    wordsBag = WordsBag(wordsDir, shortestWord, longestWord, exemptDir)
    wordsBag.read()

    # Make guesses
    guessMaker.makeGuessesFromTemplates(wordsBag.bag, guessTemplates)

    # Write to file
    guessMaker.write()

# Check if guesses are correct
if STEP == 3:
    guessMaker = GuessMaker(guessDir, guessIndices)
    guessMaker.read()

    print(guessMaker.guesses)

    for index in guessIndices:
        guessMaker.check(index, printCheck)