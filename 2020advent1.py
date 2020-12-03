import requests, os

os.environ['AOC_SESSION'] = '53616c7465645f5f1eec9f1f7ba89cd2adbf508cbf6e8989d39e3d98d1a197ffecdfb37ed0e2532810d8e29aa41fcae5'

t = requests.get('https://adventofcode.com/2020/day/1/input', cookies=dict(session=os.environ['AOC_SESSION'])).text

#data = open('foo.txt', 'r')
d = [int(i) for i in t.splitlines()]

def part1():
    for f in d:
        if (2020-int(f)) in set(d):
            print(int(f)  * (2020-int(f)))
            return

def part2():
    for x in range(0, len(d)-2): 
        for y in range(x+1, len(d)-1):
            for z in range(y+1, len(d)):
                if d[x] + d[y] + d[z] == 2020:
                    print (d[x]*d[y]*d[z])
                    return

#part1()
part2()