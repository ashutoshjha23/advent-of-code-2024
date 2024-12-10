<<<<<<< HEAD
import re

def sum(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, content)
        
        total_sum = 0
        for x, y in matches:
            total_sum += int(x) * int(y)
        
        return total_sum

    except FileNotFoundError:
        return "no file"
    except Exception as e:
        return f"error: {e}"

if __name__ == "__main__":
    file_path = "day3.txt"  
    result =sum(file_path)
    print(f"total: {result}")
=======
import re

def sum(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, content)
        
        total_sum = 0
        for x, y in matches:
            total_sum += int(x) * int(y)
        
        return total_sum

    except FileNotFoundError:
        return "no file"
    except Exception as e:
        return f"error: {e}"

if __name__ == "__main__":
    file_path = "day3.txt"  
    result =sum(file_path)
    print(f"total: {result}")
>>>>>>> 4807f15de93ff62b15742458b379a60c108eb975
