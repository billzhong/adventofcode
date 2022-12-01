with open('input.txt') as f:
    calories = f.read().strip().split('\n\n')

elves = [sum(int(i) for i in c.split('\n')) for c in calories]

print(max(elves))

print(sum(sorted(elves, reverse=True)[:3]))
