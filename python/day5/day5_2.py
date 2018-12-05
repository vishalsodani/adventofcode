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
    #print(polymer)
    last_character = ''
    found = False
    no_match_found = False
    match_found = False
    use_polymer = polymer.replace(start_at, '').replace(start_at.upper(), '')
    #print(use_polymer)
    while no_match_found == False:
        #import pdb;pdb.set_trace()
        found = False
        last_character = ''
        for index, character in enumerate(use_polymer):
            if found:
                break
            if character.lower() == last_character.lower():
                if character.isupper() and last_character.islower() or character.islower() and last_character.isupper():
                    #import pdb;pdb.set_trace()
                    new_str = use_polymer[index+1:]
                    old_str = use_polymer[0:index-1]
                    use_polymer = old_str + new_str
                    found = True

            else:
                last_character = character
        last_character_in = ''
        match_found = False
        if found == False:
            break
        #import pdb;pdb.set_trace()
        for index, character in enumerate(use_polymer):
            if character.lower() == last_character_in.lower():
                if character.isupper() and last_character.islower() or character.islower() and last_character.isupper():
                    match_found = True
                    break
            else:
                last_character_in = character
                match_found = False
        if match_found == False:
            no_match_found = True
        #if match_found:
            #break
    #print(" the length is %s on remove %s" % (len(use_polymer), start_at))
    if shortest_length == 0:
        shortest_length = len(use_polymer)
    elif len(use_polymer) < shortest_length:
        shortest_length = len(use_polymer)
    i = i + 1
    start_at = az[i]
    with open('input.txt') as fp:
        for input in fp:
            polymer = input
     
print(shortest_length)