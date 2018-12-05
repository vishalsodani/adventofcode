start_frequency = 0
track_frequency = {}
found_duplicate = False
inputs = []
with open('input.txt') as fp:
    for input in fp:
        inputs.append(int(input))
        
while found_duplicate == False:
    for freq in inputs:
        start_frequency += freq
        if start_frequency in track_frequency:
            found_duplicate = True
            print(start_frequency)
            break
        else:
            track_frequency[start_frequency] = 1


		