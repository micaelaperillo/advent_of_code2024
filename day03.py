# Advent of Code 2024 - Day 03
import re

def load_data():
    with open('day03.txt') as f:
        data = f.readlines()
        return ''.join(data)
    
def day01():
    data = load_data()
    
    regex_pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
    matches = re.findall(regex_pattern, data)
    
    result = 0
    for match in matches:
        numbers = re.findall(r'[0-9]{1,3}', match)
        result += int(numbers[0]) * int(numbers[1])
    return result

def day02():
    data = load_data()

    regex_pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(regex_pattern, data)

    result = 0
    # delete mult between dont and do
    can_mult = True
    for match in matches:
        if match == "do()":
            if not can_mult:
                can_mult = True
        elif match == "don't()":
            if can_mult:
                can_mult = False
        elif can_mult:
            numbers = re.findall(r'[0-9]{1,3}', match)
            result += int(numbers[0]) * int(numbers[1])
    return result

print(day02())