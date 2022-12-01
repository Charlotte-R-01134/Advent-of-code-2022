def getCalories(cals):
    total = 0
    for i in range(len(cals)):
        total = total + int(cals[i])
    return total

def part1():
    data = open('Day 1\day 1.txt', 'r')
    calList = data.read().strip().split("\n\n")
    data.close()
    most = 0
    for cals in calList:
        cals = cals.split("\n")
        total = getCalories(cals)
        if total > most:
            most = total
    print(most)

part1()

def part2():
    data = open('Day 1\day 1.txt', 'r')
    calList = data.read().strip().split("\n\n")
    data.close()
    # top 3 calories
    top3 = [0, 0, 0]
    for cals in calList:
        cals = cals.split("\n")
        total = getCalories(cals)
        if total > top3[0]:
            top3[2] = top3[1]
            top3[1] = top3[0]
            top3[0] = total
        elif total > top3[1]:
            top3[2] = top3[1]
            top3[1] = total
        elif total > top3[2]:
            top3[2] = total
    print(top3[0] + top3[1] + top3[2])

part2()

