def getSentences(prefix, lengths):
    sentences = list()
    if (len(lengths) == 0):
        return [prefix]
    else:
        length = lengths[0]
        if type(length) == type(""):
            return sentences + getSentences(prefix + " " + length, lengths[1:])
        
        for word in words[length]:
            sentences += getSentences(prefix + " " + word, lengths[1:])

    return sentences

words = {
    1: ["I", "A"],
    2: ["Me", "Or"],
    3: ["Hoe", "Sir", "Tab", "Net", "Pat", "Ton", "Not", "You", "Eve", "Fir", "For", "Bet", "Eat", "The", "Get", "One", "Win", "Sea", "Bat", "Tap"],
    4: ["Note", "Tabs", "Ever", "Tent", "Fore", "Leto", "Bath"],
    5: ["Think", "About", "Every", "Night", "Stone"],
    6: ["Winner", "Nights", "Stones"],
    7: ["Forever", "Nothing"]
}

lengthsList = [
    [7, 3],
    [1, 3, 3, 5, 5, 2],
    [7, 6],
    [3, 4, 5, 5]
]

for lengths in lengthsList:
    print(getSentences("", lengths))