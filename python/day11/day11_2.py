grid_serial_number = 42
range_x = 5
range_y = 5
fuel_grid = [[0 for x in range(range_x)] for y in range(range_y)]

total_cells_with_neg_power = 0
positive_power = 0
top_left_fuel = []
size_of_square = 1
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

while size_of_square < range_x + 1:
    for i in range(0, range_x):
        if size_of_square > 1 and i + size_of_square > range_x:
            continue
        for y in range(0, range_y ):
            if size_of_square > 1 and y + size_of_square > range_y:
                continue

            
            power_square = 0        
            #print("----size of square %s" % size_of_square)
            for dx in range(i, i+size_of_square):
                
                for ey in range(y, y+size_of_square):
                    if (ey <= range_x - 1) and (dx <= range_y - 1):
                        #print("%s,%s" % (dx, ey))
                        #try:
                        power_square += fuel_grid[dx][ey]
                        # except:
                        #     power_square += 0
            if power_square > positive_power:
                # print("----size of square %s" % size_of_square)
                # print(i)
                # print(y)
                # print(power_square)
                # print("---done----")
                positive_power = power_square
                top_left_fuel = []
                top_left_fuel.append(i)
                top_left_fuel.append(y)
                grid_size = size_of_square
    size_of_square = size_of_square + 1
    #import pdb;pdb.set_trace()


print(positive_power)
print(top_left_fuel)
print(grid_size)

