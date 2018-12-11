grid_serial_number = 9221
fuel_grid = [[0 for x in range(300)] for y in range(300)]
total_cells_with_neg_power = 0
positive_power = 0
top_left_fuel = []

for i in range(0, 300):
    for y in range(0, 300):
        x_index = i + 1
        y_index = y + 1
        rack_id = x_index + 10
        power_level = rack_id * y_index
        power_level += grid_serial_number
        power_level = power_level * rack_id
        try:
            hundreds = int(str(power_level)[-3:-2])
        except:
            hundreds = 0
        power_level = hundreds - 5
        fuel_grid[i][y] = power_level
        if power_level < 0:
            total_cells_with_neg_power += 1

for i in range(0, 300):
    for y in range(0, 300):
        if fuel_grid[i][y] > 0:
            power_square = 0
            for d in [i, i+1, i+2]:
                for e in [y, y+1, y+2]:
                    try:
                        power_square += fuel_grid[d][e]
                    except:
                        power_square += 0
            if power_square > positive_power:
                positive_power = power_square
                top_left_fuel = []
                top_left_fuel.append(i)
                top_left_fuel.append(y)

print(positive_power)
print(top_left_fuel)

