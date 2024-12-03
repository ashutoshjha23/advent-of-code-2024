def input(file_path):
    reports = []
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            reports.append(report)  
    return reports
def safe(report):
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False
    inc = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    dec= all(report[i] > report[i + 1] for i in range(len(report) - 1)) 
    return inc or dec

def rem(report):

    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  
        if safe(modified_report):
            return True 
    return False

def reports(file_path):
    reports = input(file_path)
    
    count = 0
    for report in reports:
        if safe(report):
            count += 1
        elif rem(report):
            count += 1
    
    return count


file_path = "day2.txt"  
safe = reports(file_path)
print(f"Num: {safe}")
