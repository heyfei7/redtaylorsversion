from ReaderWriter import *
from WordsBag import *
import requests

def readGuessTemplate(guessTemplateFile):
    templateFile = ReaderWriter(guessTemplateFile)
    templates = dict()
    for template in templateFile.read(" "):
        index = int(template[0])
        templates.setdefault(index, list())
        templates[index].append([int(x) if x.isdigit() else str(x) for x in template[1:]])
    return templates

class GuessMaker:

    def getGuessFromTemplate(self, wordsBag, template):
        def getGuesses(temp, prefix):
            if (len(temp) == 0):
                return [prefix]
            else:

                def validWord(word):
                    return len(prefix) == 0 or word != prefix[:-1]

                sentences = []
                item = temp[0]

                words = []
                if type(item) == type(""):
                    words = [item]
                else:
                    words = wordsBag[item]

                words = tuple(filter(validWord, words))            
                for word in words:
                    sentences += getGuesses(temp[1:], prefix + [word])

            return sentences
        
        return getGuesses(template, [])
    
    def makeGuessesFromTemplates(self, wordsBag, templates):
        for index, template in templates.items():
            for temp in template:
                self.guesses[index] = self.getGuessFromTemplate(wordsBag, temp)

    def __init__(self, guessDir, guessIndices):
        super().__init__()
        self.guessDir = ReaderWriterDir(guessDir, ".txt")
        self.guesses = dict()
        self.indices = guessIndices
        for index in guessIndices:
            self.guesses[index] = list()
        
    def read(self):
        self.guesses = self.guessDir.readAll(self.indices, " ")
    
    def write(self):
        self.guessDir.writeAll(self.guesses, " ")
    
    def check(self, index, checker):
        for guess in self.guesses[index]:
            checker(index, guess)

url = 'https://redtaylorsversion.taylorswift.com/api/words'

def taylorSwiftCheck(index, guess):
    guess = [x.lower() for x in guess]
    myobj = {'row': guess, 'rowInd': index}
    x = requests.post(url, data = myobj)
    if (not ('rowCorrect' in x.text)) or (not ("false" in x.text)):
        print(x.text, index, " ".join(guess))

def printCheck(index, guess):
    print(index, " ".join(guess))