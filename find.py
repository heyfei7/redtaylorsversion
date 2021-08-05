import enchant

englishDictionary = enchant.Dict("en_US")   

# Words

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

def getWordsOfLength(strings, wordLength):
    words = set()
    for string in strings:
        words = words.union(getWordsFromString(string, wordLength))
    return words

# Sentences

def getSentencesOfLengths(lengthToWords, exempt, lengths):

    def validWord(word):
        return not (word in exempt)

    def getSentences(lengths, prefix):
        if (len(lengths) == 0):
            return [prefix]
        else:
            sentences = []
            length = lengths[0]

            words = []
            if type(length) == type(""):
                words = [length]
            else:
                words = lengthToWords[length]

            words = tuple(filter(validWord, words))            
            for word in words:
                sentences += getSentences(lengths[1:], prefix + [word])

        return sentences
    
    sentences = getSentences(lengths, [])
    return [" ".join(x) for x in sentences]