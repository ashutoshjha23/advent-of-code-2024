def read_map(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

def move_guard(lab_map):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    rows, cols = len(lab_map), len(lab_map[0])
    visited = set()
    
    for r in range(rows):
        for c in range(cols):
            if lab_map[r][c] in directions:
                x, y = r, c
                direction = lab_map[r][c]
                break
    
    while 0 <= x < rows and 0 <= y < cols:
        visited.add((x, y))
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < rows and 0 <= ny < cols and lab_map[nx][ny] == '#':
            direction = turns[direction]
        else:
            x, y = nx, ny
    
    return visited

def main():
    file_path = input("Enter the path to the input file: ")
    lab_map = read_map(file_path)
    visited_positions = move_guard(lab_map)
    print(len(visited_positions))

if __name__ == "__main__":
    main()
