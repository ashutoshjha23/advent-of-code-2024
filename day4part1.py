def count(grid):
    def word(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
                return 0
        return 1

    word = "XMAS"
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0), 
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    tot = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                tot += word(x, y, dx, dy)
    return tot


if __name__ == "__main__":
    file_path = "day4.txt"
    try:
        with open(file_path, 'r') as file:
            grid = [list(line.strip()) for line in file.readlines()]

        result = count(grid)
        print(f"Total: {result}")
    except FileNotFoundError:
        print("file nahi mil raha")
    except Exception as e:
        print(f"error: {e}")
