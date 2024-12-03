from collections import Counter
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

def sco(left_list, right_list):
    right_counts = Counter(right_list)

    score = sum(left * right_counts[left] for left in left_list)  
    return score
file_path = "day1.txt"  
left_list, right_list = input(file_path)
score = sco(left_list, right_list)
print(f"score: {score}")
