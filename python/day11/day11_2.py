grid_serial_number = 9221
range_x = 300
range_y = 300
fuel_grid = [[0 for x in range(range_x)] for y in range(range_y)]

total_cells_with_neg_power = 0
positive_power = 0
top_left_fuel = []
size_of_square = 9
grid_size = 0

for i in range(0, range_x):
    for y in range(0, range_y):
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

while size_of_square < 13:
    for i in range(0, range_x):
        if size_of_square > 1 and i + size_of_square > range_x:
            continue
        for y in range(0, range_y ):
            if size_of_square > 1 and y + size_of_square > range_y:
                continue
            power_square = 0        
            for dx in range(i, i+size_of_square):
                for ey in range(y, y+size_of_square):
                    if (ey <= range_x - 1) and (dx <= range_y - 1):
                        power_square += fuel_grid[dx][ey]
            if power_square > positive_power:
                positive_power = power_square
                top_left_fuel = []
                top_left_fuel.append(i)
                top_left_fuel.append(y)
                grid_size = size_of_square
    size_of_square = size_of_square + 1


print(positive_power)
print(top_left_fuel)
print(grid_size)

