def playGame(play):
    # A = Rock, B = Paper, C = Scissors
    # Y = Paper, X = Rock, Z = Scissors
    scores = {"X": 1, "Y": 2, "Z": 3}
    wins = [["A", "Y"], ["B", "Z"], ["C", "X"]]
    draws = [["A", "X"], ["B", "Y"], ["C", "Z"]]
    if play in wins:
        return scores[play[1]]+6
    elif play in draws:
        return scores[play[1]]+3
    else:
        return scores[play[1]]


def part1():
    # open file and split by new line
    data = open('Day 2\input.txt', 'r')
    playList = data.read().strip().split("\n")
    data.close()
    total = 0
    for play in playList:
        # split by space
        play = play.split(" ")
        game = playGame(play)
        total = total + game

    print(total)

part1()

def playWithStrategy(play):
    # A = Rock, B = Paper, C = Scissors
    # Y = draw, X = lose, Z = win
    wins = [["A", "Y"], ["B", "Z"], ["C", "X"]]
    draws = [["A", "X"], ["B", "Y"], ["C", "Z"]]
    lose = [["A", "Z"], ["B", "X"], ["C", "Y"]]
    if play[1] == "X":
        # lose
        # play game where you lose
        if play[0] == "A":
            # return corrosponding lose pair
            return playGame(lose[0])
        elif play[0] == "B":
            return playGame(lose[1])
        else:
            return playGame(lose[2])
    elif play[1] == "Y":
        # draw
        if play[0] == "A":
            # return corrosponding draw pair
            return playGame(draws[0])
        elif play[0] == "B":
            return playGame(draws[1])
        else:
            return playGame(draws[2])
    else:
        # win
        if play[0] == "A":
            # return corrosponding win pair
            return playGame(wins[0])
        elif play[0] == "B":
            return playGame(wins[1])
        else:
            return playGame(wins[2])

def part2():
    # open file and split by new line
    data = open('Day 2\input.txt', 'r')
    playList = data.read().strip().split("\n")
    data.close()
    total = 0
    for play in playList:
        # split by space
        play = play.split(" ")
        game = playWithStrategy(play)
        total = total + game

    print(total)

part2()