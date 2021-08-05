import requests
import file

url = 'https://redtaylorsversion.taylorswift.com/api/words'

def printGuessResult(guess, index, result):
    print(result, index, " ".join(guess))

def checkGuess(index, guess):
    guess = [x.lower() for x in guess]
    myobj = {'row': guess, 'rowInd': index}
    x = requests.post(url, data = myobj)
    if (not ('rowCorrect' in x.text)) or (not ("false" in x.text)):
        print(x.text, index, " ".join(guess))