from collections import defaultdict

def find_antinodes(map):
    height = len(map)
    width = len(map[0])
    antenna_locations = defaultdict(list)
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char != '.':
                antenna_locations[char].append((x, y))

    antinodes = set()
    for freq, coords in antenna_locations.items():
        for i, (x1, y1) in enumerate(coords):
            for j in range(i + 1, len(coords)):
                x2, y2 = coords[j]
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0 or dy == 0: 
                    for k in range(min(y1, y2), max(y1, y2) + 1):
                        antinodes.add((x1, k))
                    for k in range(min(x1, x2), max(x1, x2) + 1):
                        antinodes.add((k, y1))
    return len(antinodes)

if __name__ == "__main__":
    with open("day8.txt", "r") as f:
        map_data = f.read().splitlines()
    result = find_antinodes(map_data)
    print(result)