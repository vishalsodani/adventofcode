fn main() {
    let grid_serial_number = 9221;
    let mut fuel_grid = vec![vec![0; 300]; 300];
    let mut positive_power = 0;
    let mut top_left_fuel = Vec::new();

    for i in 0..300 {
        for y in 0..300 {
            let x_index = i + 1;
            let y_index = y + 1;
            let rack_id = x_index + 10;
            let mut power_level = ((rack_id * y_index) + grid_serial_number) * rack_id;
            let mut hundreds: i32 = 0;
            let pls = power_level.to_string();
            let mut rp = pls.chars();    
            let count = power_level.to_string().chars().count() - 2;
            for dd in 0..count {
                if dd < count - 1 {
                    rp.next();
                }
                else{
                    hundreds = rp.next().unwrap().to_string().parse::<i32>().unwrap();
                }
            }
            fuel_grid[i][y] = hundreds - 5;
        }
    }

    for i in 0..300 {
        for y in 0..300 {
            if fuel_grid[i][y] > 0 {
                let mut power_square = 0;
                for d in vec![i, i+1, i+2]
                {
                    for e in vec![y, y+1, y+2]{
                        if e < 300 && d < 300 {
                            power_square += fuel_grid[d][e];
                        }
                        
                    }
                }
                if power_square > positive_power {
                    positive_power = power_square;
                    top_left_fuel = Vec::new();
                    top_left_fuel.push(i);
                    top_left_fuel.push(y);
                }
            }
        }
    }

    println!("{}", positive_power);
    println!("{:?}", top_left_fuel);
}