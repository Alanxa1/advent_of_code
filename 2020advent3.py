import requests, os

os.environ['AOC_SESSION'] = '53616c7465645f5f1eec9f1f7ba89cd2adbf508cbf6e8989d39e3d98d1a197ffecdfb37ed0e2532810d8e29aa41fcae5'

t = requests.get('https://adventofcode.com/2020/day/3/input', cookies=dict(session=os.environ['AOC_SESSION'])).text

#data = open('foo.txt', 'r')
d = [i for i in t.splitlines()]
treehitcount = 0
marker = 0

def part1(increment):
    global marker
    global treehitcount
    for path in d:
        if marker >= len(path):
            marker -= len(path)
        if path[marker] == '#':
            treehitcount += 1
        marker += increment
    print(treehitcount)

def part2():
    global marker
    global treehitcount
    for index, path in enumerate(d):
        if index % 2 == 0:
            if marker >= len(path):
                marker -= len(path)
            if path[marker] == '#':
                treehitcount += 1
            marker += 1
    print(treehitcount)

part1(3)