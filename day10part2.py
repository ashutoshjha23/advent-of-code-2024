def find_trails(coords, tile, height_map):
    y, x = coords
    if 0 <= y < len(height_map) and 0 <= x < len(height_map[0]) and height_map[y][x] == tile:
        if tile == '9':
            return 1  
        next_tile = chr(ord(tile) + 1)  
        return sum([
            find_trails((y + dy, x + dx), next_tile, height_map)
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ])
    return 0
with open("day10.txt", "r") as file:
    data = [line.rstrip("\n") for line in file.readlines()]
    total_paths = 0
    for y, row in enumerate(data):
        for x, tile in enumerate(row):
            if tile == "0":
                total_paths += find_trails((y, x), "0", data)
    print(total_paths)