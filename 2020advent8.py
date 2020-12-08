import os, requests, re
from collections import defaultdict

t = requests.get('https://adventofcode.com/2020/day/8/input', cookies=dict(session=os.environ['AOC_SESSION'])).text[:-1]

def part1():
    commandnumber = 0
    accumulator = 0
    tracker = defaultdict(int)
    data = t.splitlines()
    while True:
        m = re.search(r'([a-z]{3})\s(\+?-?\d+)', data[commandnumber])
        tracker[data[commandnumber]+str(commandnumber)] += 1
        if tracker[data[commandnumber]+str(commandnumber)] > 1:
            print("Boot sequence was about to run twice with command {}, accumulator is at {}".format(data[commandnumber], accumulator))
            break
        elif m[1] == "jmp": 
            commandnumber += int(m[2])
        elif m[1] == "acc": 
            accumulator += int(m[2])
            commandnumber += 1
        elif m[1] == "nop": 
            commandnumber += 1 

def part2():
    x = 0 
    commandnumber = 0
    accumulator = 0
    tracker = defaultdict(int)
    while True:
        data = t.splitlines()
        if data[x].startswith("nop"):
            data[x] = "jmp"+data[x][3:]
        elif data[x].startswith("jmp"):
            data[x] = "nop"+data[x][3:] 
        m = re.search(r'([a-z]{3})\s(\+?-?\d+)', data[commandnumber])
        tracker[data[commandnumber]+str(commandnumber)] += 1
        if data[commandnumber]+str(commandnumber) == 'jmp +1636':
            print("Boot sequence has ended {} {}, accumulator is at {}".format(data[commandnumber], str(commandnumber), accumulator))
            #print(data[commandnumber]+str(commandnumber), accumulator)
            break
        elif tracker[data[commandnumber]+str(commandnumber)] > 1:
            #print("Boot sequence was about to run twice with command {}, accumulator is at {}".format(data[commandnumber], accumulator))
            tracker = defaultdict(int)
            accumulator = 0
            commandnumber = 0
            x += 1
            continue
        elif m[1] == "jmp": 
            commandnumber += int(m[2])
        elif m[1] == "acc": 
            accumulator += int(m[2])
            commandnumber += 1
        elif m[1] == "nop": 
            commandnumber += 1 

part1()
part2()