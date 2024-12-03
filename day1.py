def input(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)
    
    return left_list, right_list

def td(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    
    return total_distance
file_path = "day1.txt" 
left_list, right_list = input(file_path)
result = td(left_list, right_list)
print(f"distance: {result}")