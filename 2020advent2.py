import requests, os, re

os.environ['AOC_SESSION'] = '53616c7465645f5f1eec9f1f7ba89cd2adbf508cbf6e8989d39e3d98d1a197ffecdfb37ed0e2532810d8e29aa41fcae5'

t = requests.get('https://adventofcode.com/2020/day/2/input', cookies=dict(session=os.environ['AOC_SESSION'])).text
count = 0

def part1():
    global count
    for line in t.splitlines():
        m = re.search(r'(\d+)-(\d+)\s(\w):\s(\w+)', line)
        password = m.group(4)
        lowerbound = int(m.group(1))
        upperbound = int(m.group(2))
        counter = password.count(m.group(3))
        if counter >= lowerbound and counter <= upperbound:
            count += 1
    print(count)

def part2():
    global count
    for line in t.splitlines():
        m = re.search(r'(\d+)-(\d+)\s(\w):\s(\w+)', line)
        password = m.group(4)
        pos1 = int(m.group(1))
        pos2 = int(m.group(2))
        letter = m.group(3)
        if password[pos1-1] == letter and not password[pos2-1] == letter:
            count += 1
        if password[pos2-1] == letter and not password[pos1-1] == letter:
            count += 1
    print(count)

part2()
