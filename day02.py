# Advent of Code 2024 - Day 02

def load_data():
    reports = []
    with open("day02.txt") as f:
        data = f.readlines()
        for line in data:
            reports.append(line.strip())

    return reports

def check_report(r):
    asc = all(1 <= r[i] - r[i-1] <= 3 for i in range(1, len(r))) 
    desc = all(1 <= r[i-1] - r[i] <= 3 for i in range(1, len(r)))
    return asc or desc

def check_report_2(r):
    if check_report(r):
        return check_report(r)
    for i in range(len(r)):
        rep = r[:i] + r[i + 1:]
        asc = all(1 <= rep[j] - rep[j - 1] <= 3 for j in range(1, len(rep)))
        desc = all(1 <= rep[j - 1] - rep[j] <= 3 for j in range(1, len(rep)))
        if asc or desc:
            return True 
    return False

def part01():
    reports = load_data()
    safe_reports = 0

    for r in reports:
        r = r.split(" ")
        r = list(map(int, r))
        safe_reports += check_report(r)
    return safe_reports

def part02():
    reports = load_data()
    safe_reports = 0

    for r in reports:
        r = r.split(" ")
        r = list(map(int, r))
        safe_reports += check_report_2(r)

    return safe_reports


            
            


