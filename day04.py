# Advent of Code 2024 - Day 04

def load_data():
    with open('day04.txt') as f:
        data = f.readlines()
        return [list(line.strip()) for line in data]

def part01():
    data = load_data()
    
    directions = [
        (1, -1),
        (1, 0),
        (1, 1),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 0),
        (-1, 1)
    ]

    word = "XMAS"
    word_length = len(word)
    xmas_count = 0

    rows = len(data)
    cols = len(data[0])

    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                 if 0 <= r + dx * (word_length - 1) < rows and 0 <= c + dy * (word_length - 1) < cols:
                    found_word = ''.join(data[r + i * dx][c + i * dy] for i in range(word_length))
                    if found_word == word:
                        xmas_count += 1

    return xmas_count

def part02():
    data = load_data()

    words = ['SAM', 'MAS']  

    xmas_count = 0

    rows = len(data)
    cols = len(data[0])

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            center = data[r][c]
            if center != 'A':
                continue
            top_left = data[r - 1][c - 1]
            top_right = data[r - 1][c + 1]
            bottom_left = data[r + 1][c - 1]
            bottom_right = data[r + 1][c + 1]
            first_word = top_left + center + bottom_right
            second_word = bottom_left + center + top_right
            if first_word in words and second_word in words:
                xmas_count += 1

    return xmas_count
    