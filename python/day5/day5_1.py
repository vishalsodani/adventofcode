polymer = ''
with open('input.txt') as fp:
    for input in fp:
        polymer = input

no_match_found = False
polymer = list(polymer)

while no_match_found == False:
    found = False
    next_input = []
    skip_index = -1
    for index, character in enumerate(polymer):
        if index == skip_index:
            skip_index = -1
            continue
        try:
            next_character = polymer[index + 1]
            if character.lower() == next_character.lower():
                if character.isupper() and next_character.islower() or character.islower() and next_character.isupper():
                    found = True
                    skip_index = index + 1
                else:
                    next_input.append(character)
            else:
                next_input.append(character)
        except:
            next_input.append(character)
    polymer = next_input
    if found == False:
        break
print(len(polymer))

        
     