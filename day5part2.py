def parse_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    rs, us = content.split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in rs.strip().split('\n')]
    updates = [list(map(int, line.split(','))) for line in us.strip().split('\n')]

    return rules, updates


def vali(update, rules):
    pi = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in pi and y in pi:
            if pi[x] > pi[y]:
                return False
    return True


def ru(update, rules):
    graph = {page: set() for page in update}
    in_degree = {page: 0 for page in update}

    for x, y in rules:
        if x in graph and y in graph:
            if y not in graph[x]:
                graph[x].add(y)
                in_degree[y] += 1

    queue = [page for page in update if in_degree[page] == 0]
    ordered_update = []

    while queue:
        current = queue.pop(0)
        ordered_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered_update


def mid_sum(file_path):
    rules, updates = parse_input(file_path)
    mid_sum = 0

    for update in updates:
        if not vali(update, rules):
            update = ru(update, rules)
            mid_index = len(update) // 2
            mid_sum += update[mid_index]

    return mid_sum


if __name__ == "__main__":
    file_path = "day5.txt "
    try:
        result = mid_sum(file_path)
        print(f"sum: {result}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"error: {e}")
