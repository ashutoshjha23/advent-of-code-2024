def read_disk_map(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def move_files_to_left(disk_map):
    blocks = []
    file_id = 0
    
    i = 0
    while i < len(disk_map):
        file_length = int(disk_map[i])
        blocks.extend([file_id] * file_length)
        file_id += 1
        i += 1
    
    compacted_blocks = [file_id for file_id in blocks if file_id != '.']
    
    free_space_count = len(disk_map) - len(compacted_blocks)
    compacted_blocks = ["."] * free_space_count + compacted_blocks
    
    return "".join(str(block) for block in compacted_blocks)

def calculate_checksum(disk_map):
    checksum = 0
    for i, block in enumerate(disk_map):
        if block != '.':
            checksum += i * int(block)
    return checksum

def main():
    file_path = input("Enter the path to the input file: ").strip()
    disk_map = read_disk_map(file_path)
    
    compacted_disk = move_files_to_left(disk_map)
    
    checksum = calculate_checksum(compacted_disk)
    
    print(f"Resulting checksum: {checksum}")

if __name__ == "__main__":
    main()
