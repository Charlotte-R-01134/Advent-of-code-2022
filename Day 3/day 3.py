from string import ascii_letters

def part1():
    with open('Day 3\input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    total = 0
    for line in lines:
        mid = len(line) // 2
        left = line[:mid]
        right = line[mid:]
        # find elements in left that are also in right
        common = set(left).intersection(set(right)) 
        # find denary value of each common element
        common = [ascii_letters.index(c) + 1 for c in common]
        total = total + sum(common)
    print(total)

part1()

def part2():
    with open('Day 3\input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    total = 0
    for i in range(0, len(lines), 3): # step by 3
        group = lines[i:i+3]
        common = set(group[0]).intersection(set(group[1]), set(group[2]))
        total = total + sum([ascii_letters.index(c) + 1 for c in common])
    print(total)

part2()