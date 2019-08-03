import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def definition(w):
    w = w.casefold()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        response = input("Did you mean %s instead?\nY for yes N for no: " % get_close_matches(w, data.keys())[0])
        if response.lower() == "y":
            return data[get_close_matches(w, data.keys())[0]]

        elif response.lower() == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We did not understand your query."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter Word: ")

output = definition(word)

if type(output) == list:
    count = 1
    for i in output:
        print(str(count) + ". " + i)
        count = count + 1
else:
    print(output)







