import numpy
serial_number = 6392

grid = numpy.zeros((300,300))

def find_power(x, y, serial_number):
    rack_id = x+10
    power_level = rack_id*y
    power_level += serial_number
    power_level *= rack_id
    power_level = (power_level//100)%10
    power_level -= 5
    return power_level

def power_sum(x,y,size):
    power = 0
    for i in range(size):
        for j in range(size):
            power += grid[x + i][y + j]
    return power

def fill_grid(serial_number):
    for x in range(300):
        for y in range(300):
            grid[x][y] = find_power(x+1,y+1,serial_number)

def part_one():
    max_power = -1e9
    cell = None
    for x in range(297):
        for y in range(297):
            power = power_sum(x, y, 3)
            if power > max_power:
                max_power = power
                cell = (x+1, y+1)
    print(cell)

fill_grid(serial_number)
part_one()

def part_two():
    max_power = -1e9
    cell = None
    for s in range(300):
        for x in range(300-s):
            for y in range(300-s):
                power = power_sum(x,y,s)
                power = grid[x:x+s, y:y+s].sum()
                if power > max_power:
                    max_power = power
                    cell = (x+1, y+1,s)
    print(cell)

part_two()
