lines = open('day12_input.txt').read().strip().split('\n')
init = "#.##.#.#...#......#..#.###..##...##.#####..#..###.########.##.....#...#...##....##.#...#.###...#.##"
rules = {}

def sum_plants(curr):
    diff = (len(curr) - len(init)) // 2
    sum = 0
    for i, c in enumerate(curr):
        if c == '#':
            sum += (i - diff)
    return sum

for i in range(2,len(lines)):
    curr, next = lines[i].split("=>")
    rules[curr.strip()] = next.strip()
    
def part1():
    for x in range(25):
        curr = "...."+init+"...."
        next = ""
        for x in range(2, len(curr) - 2):
            sub = curr[x-2:x+3]
            next+= rules[sub]
            next += rules[sub]
        curr = next
    print(sum_plants(curr))

part1()
