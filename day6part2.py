def read_map(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

def simulate_guard(lab_map, obstruction=None):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    rows, cols = len(lab_map), len(lab_map[0])
    visited = set()
    path = set()

    for r in range(rows):
        for c in range(cols):
            if lab_map[r][c] in directions:
                x, y = r, c
                direction = lab_map[r][c]
                break

    if obstruction:
        lab_map[obstruction[0]][obstruction[1]] = '#'

    while (x, y, direction) not in path:
        if not (0 <= x < rows and 0 <= y < cols):
            return False
        path.add((x, y, direction))
        visited.add((x, y))
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        if 0 <= nx < rows and 0 <= ny < cols and lab_map[nx][ny] == '#':
            direction = turns[direction]
        else:
            x, y = nx, ny

    return True

def find_valid_obstruction_positions(lab_map):
    rows, cols = len(lab_map), len(lab_map[0])
    valid_positions = 0

    for r in range(rows):
        for c in range(cols):
            if lab_map[r][c] == '.':
                lab_copy = [row[:] for row in lab_map]
                if simulate_guard(lab_copy, obstruction=(r, c)):
                    valid_positions += 1

    return valid_positions

def main():
    file_path = input("Enter the path to the input file: ")
    lab_map = read_map(file_path)
    result = find_valid_obstruction_positions(lab_map)
    print(result)

if __name__ == "__main__":
    main()
