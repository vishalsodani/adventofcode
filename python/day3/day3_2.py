elves_plan = {}
inputs = []
i = 0
with open('input.txt') as fp:
    for input in fp:
        
        input = input.split()
        elves_id = input[0]
        plans = input[2].split(',')
        left_edge = int(plans[0]) + 1
        top_edge = int(plans[1][0:-1]) + 1
        total_area = input[3].split('x')
        elves_plan[elves_id] = [left_edge, top_edge, int(total_area[0]), int(total_area[1])]
        
#print(elves_plan)
seen_coordinates = set()
overlapping_coordinates = set()
for key, value in elves_plan.iteritems():
    input_is = value
    for x in range(1, value[2] + 1):
        for y in range(1, value[3] + 1):
            coordinates = (value[0] + x, value[1] + y)
            if coordinates in seen_coordinates:
                overlapping_coordinates.add(coordinates)
            else:
                seen_coordinates.add(coordinates)
#print(overlapping_coordinates)
for key, value in elves_plan.iteritems():
    input_is = value
    seen_any = False
    for x in range(1, value[2] + 1):
        for y in range(1, value[3] + 1):
            coordinates = (value[0] + x, value[1] + y)
            if coordinates in overlapping_coordinates:
                seen_any = True
    if seen_any == False:
        print(key)

		