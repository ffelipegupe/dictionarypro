import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean?: %s" %get_close_matches(word, data.keys())[0])
        ans = input("yes/no: ")
        if ans == "yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif ans == "no":
            return("Sorry, word not found")
        else:
            return("Wrong input")
    else:
        return("Word not found")

word = input("Enter the word: ")
output = search(word)
if type(output) == list:
        for item in output:
            print("Definition: ", item)
elif output == "Word not found" or output == "Sorry, word not found":
    print("Sorry, word not found")
elif output == "Wrong input":
    print("Sorry, yes or no not entered")
else:
    print("Definition: ", output)
