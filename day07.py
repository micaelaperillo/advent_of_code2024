# Advent of Code 2024 - Day 07

from itertools import product

def load_data():
    with open("day07.txt") as file:
        data = file.read().splitlines()
    return data

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i+1]
        elif operators[i] == "*":
            result *= numbers[i+1]
    return result

def part01():
    data = load_data()

    simbols = { "*", "+" }
    total_calibration_result = 0

    for line in data:
        target, numbers = line.split(":")
        target = int(target)
        numbers = numbers.split(" ")
        numbers.pop(0)
        numbers = [int(n) for n in numbers]

        operator_combinations = product(["+", "*"], repeat=len(numbers)-1)
        
        valid = False
        for operators in operator_combinations:
            result = evaluate_expression(numbers, operators)
            if result == target:
                valid = True
                break

        if valid:
            total_calibration_result += target

    return total_calibration_result
        

def part02():
    data = load_data()
    total_calibration_result = 0

    for line in data:
        target, numbers = line.split(":")
        target = int(target)
        numbers = [int(n) for n in numbers.split()]
        
        operator_combinations = product(["+", "*", "||"], repeat=len(numbers)-1)
        
        valid = False
        for operators in operator_combinations:
            result = evaluate_expression_two(numbers, operators)
            if result == target:
                valid = True
                break

        if valid:
            total_calibration_result += target

    return total_calibration_result

def evaluate_expression_two(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i+1]
        elif operators[i] == "*":
            result *= numbers[i+1]
        elif operators[i] == "||":
            result = int(str(result) + str(numbers[i+1]))
    return result