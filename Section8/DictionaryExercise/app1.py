"""
Section 8 exercise:
Use json and difflib libs to find if words entered by user
    are present in a dictionary data file presented by course.
    Followed along.

Searches keys of dict. Python easily loads json to dict
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json")) #dictionary

def translate(w):
    w = w.lower() #make input insensitive; lookup data is lowercase
    u = w[0].upper() + w[1:] #for proper nouns; try capitalizing first letter

    if w in data:
        return data[w]
    elif u in data: #could alternatively have used the str.title() function.
        return data[u]
    elif len(get_close_matches(w, data.keys())) > 0: #account for near-misses
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]) #is this a duplicate call?
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist in our dataset. Please double check it." #in lieu of getting to bottom of loop
        else:
            return "We didn't understand your entry." #out of binary Y/N
    else:
        return "The word doesn't exist in our dataset. Please double check it."

word = input("Enter word: ") #begin: user input

output = translate(word) #function call

if type(output) == list: #how to deal with >1 definition returned as list. Use type() in debugging!
    for item in output:
        print(item)
else:
    print(output)
