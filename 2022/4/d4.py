with open('input.txt') as f:
    pairs = [tuple(p.split(',')) for p in f.read().strip().split('\n')]

total1 = 0
total2 = 0

for first, second in pairs:
    f1, f2 = first.split('-')
    s1, s2 = second.split('-')

    first_range = set(range(int(f1), int(f2) + 1))
    second_range = set(range(int(s1), int(s2) + 1))

    result1 = first_range.issubset(second_range) or first_range.issuperset(second_range)
    total1 += 1 if result1 else 0

    result2 = first_range.intersection(second_range)
    total2 += 1 if result2 else 0

print(total1)
print(total2)
