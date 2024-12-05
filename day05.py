# Advent of Code 2024 - Day 5

def load_data():
    with open('day05.txt', 'r') as f:
        data = f.readlines()
        rules = []
        updates = []
        for line in data:
            line = line.strip()
            if "|" in line:
                x, y = line.split("|")
                rules.append((int(x), int(y)))
            elif line:
                updates.append([int(x) for x in line.split(",") if x.strip()])
        return rules, updates
    
def part01():
    rules, updates = load_data()
    middle_sum = 0

    for update in updates:
        valid = True  
        for x, y in rules:
            if x in update and y in update:
                index_x = update.index(x)
                index_y = update.index(y)
                if index_x >= index_y: 
                    valid = False
                    break
        
        if valid:
            middle_sum += int(update[len(update) // 2])
    return middle_sum

def fix_update(rules, update):
    update = list(update) 
    swapped = True
    while swapped:
        swapped = False
        for x, y in rules:
            if x in update and y in update:
                index_x = update.index(x)
                index_y = update.index(y)
                if index_x > index_y: 
                    update[index_x], update[index_y] = update[index_y], update[index_x]
                    swapped = True
    return update

def part02():
    middle_sum = 0
    rules, updates = load_data()
    incorrect_updates = []
    for update in updates:
        for x, y in rules:
            if x in update and y in update:
                if update.index(x) >= update.index(y): 
                    incorrect_updates.append(update)
                    break

    for update in incorrect_updates:
        fixed_update = fix_update(rules, update)
        middle_sum += fixed_update[len(fixed_update) // 2] 

    return middle_sum
