def parse_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    rs, us = content.split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in rs.strip().split('\n')]
    updates = [list(map(int, line.split(','))) for line in us.strip().split('\n')]

    return rules, updates


def vali(update, rules):
    page = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in page and y in page:
            if page[x] > page[y]:
                return False
    return True


def mid_sum(file_path):
    rules, updates = parse_input(file_path)
    mid_sum = 0

    for update in updates:
        if vali(update, rules):
            mid_index = len(update) // 2
            mid_sum += update[mid_index]                          

    return mid_sum


if __name__ == "__main__":
    file_path = "day5.txt"
    try:
        result = mid_sum(file_path)
        print(f"ssum: {result}")
    except FileNotFoundError:
        print("no file bruh.")
    except Exception as e:
        print(f"error: {e}")
