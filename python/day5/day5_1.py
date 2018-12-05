polymer = ''
import time
with open('input.txt') as fp:
    for input in fp:
        polymer = input

last_character = ''
no_match_found = False
polymer = list(polymer)

while no_match_found == False:
    found = False
    last_character = ''
    index_found = []
    for index, character in enumerate(polymer):
        if character.lower() == last_character.lower():
            if character.isupper() and last_character.islower() or character.islower() and last_character.isupper():
                index_found.append(index)
                index_found.append(index-1)
                found = True
                last_character = ''
                
        else:
            last_character = character
    for ind in sorted(index_found, reverse=True):
        del polymer[ind]
    if found == False:
        break
print(len(polymer))

        
     