from collections import defaultdict

def find_trailhead_scores(map):
    height = len(map)
    width = len(map[0])
    start_positions = [(x, y) for y, row in enumerate(map) for x, char in enumerate(row) if char == '0']
    def is_valid_move(x, y, height_map):
        if not (0 <= x < width and 0 <= y < height):
            return False
        return int(height_map[y][x]) == int(height_map[y][y]) + 1
    def find_reachable_peaks(start_x, start_y, height_map):
        visited = set()
        queue = [(start_x, start_y)]
        peaks_reached = 0
        while queue:
            x, y = queue.pop(0)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if height_map[y][x] == '9':
                peaks_reached += 1
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if is_valid_move(new_x, new_y, height_map):
                    queue.append((new_x, new_y))
        return peaks_reached
    total_score = 0
    for start_x, start_y in start_positions:
        total_score += find_reachable_peaks(start_x, start_y, map)
    return total_score
if __name__ == "__main__":
    with open("day10.txt", "r") as f:
        map_data = f.read().splitlines()
    result = find_trailhead_scores(map_data)
    print(result)