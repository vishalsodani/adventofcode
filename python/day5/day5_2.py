import string
polymer = ''
with open('input.txt') as fp:
    for input in fp:
        polymer = input


az = string.ascii_lowercase[:26]
shortest_length = 0
i = 0
start_at = 'a'

while start_at != 'z':
    no_match_found = False
    use_polymer = list(polymer.replace(start_at, '').replace(start_at.upper(), ''))
    while no_match_found == False:
        last_character = ''
        index_found = []
        for index, character in enumerate(use_polymer):
            if character.lower() == last_character.lower():
                if character.isupper() and last_character.islower() or character.islower() and last_character.isupper():
                    index_found.append(index)
                    index_found.append(index-1)
                    last_character = ''
            else:
                last_character = character
        for ind in sorted(index_found, reverse=True):
            del use_polymer[ind]
        if len(index_found) == 0:
            if shortest_length == 0:
                shortest_length = len(use_polymer)
            elif len(use_polymer) < shortest_length:
                shortest_length = len(use_polymer)
            break
    i = i + 1
    start_at = az[i]
    with open('input.txt') as fp:
        for input in fp:
            polymer = input
     
print(shortest_length)