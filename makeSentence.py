words = {
    1: ["I", "A"],
    2: ["Me", "Or"],
    3: ["Hoe", "Sir", "Tab", "Net", "Pat", "Ton", "Not", "You", "Eve", "Fir", "For", "Bet", "Eat", "The", "Get", "One", "Win", "Sea", "Bat", "Tap"],
    4: ["Note", "Tabs", "Ever", "Tent", "Fore", "Leto", "Bath"],
    5: ["Think", "About", "Every", "Night", "Stone"],
    6: ["Winner", "Nights", "Stones"],
    7: ["Forever", "Nothing"]
}

def printSentence(prefix, lengths):
    if (len(lengths) == 0):
        print(prefix)
    else:
        length = lengths[0]
        if type(length) == type(""):
            printSentence(prefix + " " + length, lengths[1:])
            return
        
        for word in words[length]:
            printSentence(prefix + " " + word, lengths[1:])

#printSentence("", ["I", 3, 3, "Think", "About", 2])
printSentence("", [3, 4, "Every", "Night"])