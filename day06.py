# Advent of Code 2024 - Day 06

def load_data():
    with open("day06.txt") as file:
        data = file.read().splitlines()
    return data

def part01():
    data = load_data()

    for i in range(len(data)):
        if "^" in data[i]:
            initial_position = (i, data[i].index("^"))

    directions = [
        (-1, 0),
        (0, 1), 
        (1, 0), 
        (0, -1) 
    ]

    x, y = initial_position
    distinct_visited = set()
    distinct_visited.add((x, y))

    rows = len(data)
    cols = len(data[0])
    dir_counter = 0

    while x in range(rows) and y in range(cols):
        i = x + directions[dir_counter][0]
        j = y + directions[dir_counter][1]
        if 0 <= i < rows and 0 <= j < cols:
            if data[i][j] == "#": 
                dir_counter = (dir_counter + 1) % 4
            else:  
                x, y = i, j
                distinct_visited.add((x, y))
        else:
            break
    return len(distinct_visited)

def part02():
    dir = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]
    si, sj = 0, 0

    data = list(list(line.strip()) for line in load_data())
    rows = len(data)
    columns = len(data[0])

    for i in range(rows):
        for j in range(columns):
            if data[i][j] == "^":
                si, sj = (i, j)
                break

    count = 0
    for i in range(rows):
        for j in range(columns):
            if data[i][j] == "#" or data[i][j] == "^":
                continue
            data[i][j] = "#"
            seen = set()
            cd = 0
            ci, cj = si, sj
            while ci in range(rows) and cj in range(columns) and (ci, cj, cd) not in seen:
                seen.add((ci, cj, cd))
                cdir = dir[cd]
                ni, nj = ci + cdir[0], cj + cdir[1]
                if ni in range(rows) and nj in range(columns) and data[ni][nj] == "#":
                    cd = (cd + 1) % 4
                else:
                    ci, cj = ni, nj
            if (ci, cj, cd) in seen:
                count += 1
            data[i][j] = "."
    return count
