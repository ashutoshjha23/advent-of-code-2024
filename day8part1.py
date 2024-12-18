def find_antinodes(map):
    height = len(map)
    width = len(map[0])
    antenna_locations = {}
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char != '.':
                antenna_locations.setdefault(char, []).append((x, y))

    antinodes = set()
    for freq, coords in antenna_locations.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                dx = x2 - x1
                dy = y2 - y1
                if (dx == 0 and dy == 0) or (dx == 0 and dy == 0): 
                    continue  
                if abs(dx) == abs(dy) * 2:
                    mid_x = (x1 + x2) // 2
                    mid_y = (y1 + y2) // 2
                    if 0 <= mid_x < width and 0 <= mid_y < height:
                        antinodes.add((mid_x, mid_y))
    return len(antinodes)

if __name__ == "__main__":
    with open("day8.txt", "r") as f:
        map_data = f.read().splitlines()
    result = find_antinodes(map_data)
    print(result)