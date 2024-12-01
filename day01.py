# Advent of Code 2024 - Day 01

def load_data():
    left = []
    right = []

    with open('day01.txt') as f:
        data = f.readlines()
        for i in range(len(data)):
            aux = data[i].split()
            left.append(int(aux[0]))
            right.append(int(aux[1]))

    return left, right

def part01():
    left, right = load_data()

    left.sort()
    right.sort()

    difs = 0
    for i in range(len(left)):
        difs += abs(right[i] - left[i])
    
    return difs

def part02():
    left, right = load_data()

    left_dict = {}
    for i in range(len(left)):
        left_dict[left[i]] = 0

    for i in range(len(right)):
        if right[i] in left_dict:
            left_dict[right[i]] += 1
    
    similarity_score = 0
    for i in range(len(left)):
        similarity_score += left[i] * left_dict[left[i]]

    return similarity_score

print(part02())