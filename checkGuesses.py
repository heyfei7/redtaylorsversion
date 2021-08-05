import requests
import file

url = 'https://redtaylorsversion.taylorswift.com/api/words'
# myobj = {'row': ["better","man"], 'rowInd': 1}
# x = requests.post(url, data = myobj)
# print(x.text)

def printGuessResult(guess, result):
    print(result, " ".join(guess))

for index in range(1, 9):
    guesses = file.readGuessFile(index)
    for guess in guesses:
        guess = [x.lower() for x in guess]
        myobj = {'row': guess, 'rowInd': index}
        x = requests.post(url, data = myobj)
        if not ('rowCorrect' in x.text):
            print(x.text, index, guess)
        elif not ("false" in x.text):
            print(x.text, index, guess)