polymer = ''
with open('input.txt') as fp:
    for input in fp:
        polymer = input

last_character = ''

found = False
no_match_found = False
match_found = False


while no_match_found == False:
    #import pdb;pdb.set_trace()
    found = False
    last_character = ''
    for index, character in enumerate(polymer):
        if found:
            break
        if character.lower() == last_character.lower():
            if character.isupper() and last_character.islower() or character.islower() and last_character.isupper():
                new_str = polymer[index+1:]
                old_str = polymer[0:index-1]
                polymer = old_str + new_str
                found = True

        else:
            last_character = character
    last_character_in = ''
    match_found = False
    if found == False:
        break
print(len(polymer))
        
     