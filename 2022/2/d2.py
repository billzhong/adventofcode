with open('input.txt') as f:
    games = [tuple(g.strip().split(' ')) for g in f.readlines()]

score1 = {'A': 1, 'B': 2, 'C': 3}
score2 = {'X': 1, 'Y': 2, 'Z': 3}

score = 0
for g in games:
    oppo = score1[g[0]]
    your = score2[g[1]]
    result = 6 if (oppo % 3) + 1 == your else 3 if oppo == your else 0
    score += your + result
print(score)

score = 0
for g in games:
    oppo = score1[g[0]]
    outcome = score2[g[1]]
    result = 0
    if outcome == 1:
        result = oppo - 1 if oppo - 1 >= 1 else 3
    elif outcome == 2:
        result = 3 + oppo
    else:
        result = 6 + (oppo % 3) + 1
    score += result
print(score)
