import requests, os, re



d = requests.get('https://adventofcode.com/2020/day/4/input', cookies=dict(session=os.environ['AOC_SESSION'])).text
count = 0
# data = open('foo.txt')
# #print(t)
# d = data.read()
profiles = (d.split("\n\n"))
indicators = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
count = len(profiles)

def part1():
    global count
    for profile in profiles:
        for abc in indicators:
            if abc not in profile:
                count -= 1
                break
    print(count)
    

def part2():
    global count
    for profile in profiles:
        for abc in indicators:
            if abc not in profile:
                count -= 1
                break
            if not bool(re.search(r'byr:19[2-9][0-9]|byr:200[0-2]', profile)):
                count -= 1
                break
            if not bool(re.search(r'iyr:201[0-9]|iyr:2020', profile)):
                count -= 1
                break
            if not bool(re.search(r'eyr:202[0-9]|eyr:2030', profile)):
                count -= 1
                break
            if not bool(re.search(r'hgt:1[5-8][0-9]cm|hgt:19[0-3]cm|hgt:59in|hgt:6[0-9]in|hgt:7[0-6]in', profile)):
                count -= 1
                break
            if not bool(re.search(r'hcl:#([0-9|a-f]{6})(?=\s|$)', profile)):
                count -= 1
                break
            if not bool(re.search(r'ecl:[amb|blu|brn|gry|grn|hzl|oth]', profile)):
                count -= 1
                break
            if not bool(re.search(r'pid:[0-9]{9}(?=\s|$)', profile)):
                count -= 1
                break

    print(count)

part2()
