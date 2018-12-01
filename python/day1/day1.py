start_frequency = 0
track_frequqncy = []
with open('input.txt') as fp:
    for input in fp:
        start_frequency += int(input)
print(start_frequency)
		