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

def getSentencesOfLengths(lengthToWords, lengths):

    def getSentences(lengths, prefix):
        if (len(lengths) == 0):
            return [prefix]
        else:

            def validWord(word):
                return len(prefix) == 0 or word != prefix[:-1]

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