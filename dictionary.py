import json

data = json.load(open("data.json"))

def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        return (print("Word not found"))

word = input("Enter the word: ")
output = search(word)
if type(output) == list:
        for item in output:
            print("Definition: ", item)
else:
    print("Definition: ", output)
