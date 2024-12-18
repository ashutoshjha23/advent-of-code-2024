from itertools import product
def evaluate_equation(equation, operators):
  numbers = [int(x) for x in equation.split()]
  result = numbers[0]
  for num, op in zip(numbers[1:], operators):
    if op == '+':
      result += num
    else:
      result *= num
  return result

def check_equation(equation, target):
  for operators in product(['+', '*'], repeat=len(equation.split()) - 1):
    if evaluate_equation(equation, operators) == target:
      return True
  return False

def calculate_calibration_result(input_file):
  with open(input_file, 'r') as f:
    return sum(
        int(line.split(': ')[0]) 
        for line in f 
        if check_equation(line.split(': ')[1], int(line.split(': ')[0]))
    )

if __name__ == "__main__":
  input_file = "day7.txt" 
  print(calculate_calibration_result(input_file))