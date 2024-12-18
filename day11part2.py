def simulate_stone_transformations(initial_stones, num_blinks):
    stones = initial_stones.copy()
    for _ in range(num_blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                half_length = len(str(stone)) // 2
                new_stones.append(int(str(stone)[:half_length]))
                new_stones.append(int(str(stone)[half_length:]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        initial_stones = [int(x) for x in f.readline().split()] 
    num_blinks = 75  
    num_stones_after_blinks = simulate_stone_transformations(initial_stones, num_blinks)
    print(f"Number of stones after {num_blinks} blinks:", num_stones_after_blinks)