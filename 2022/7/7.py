from collections import defaultdict

with open('input.txt') as f:
    disk = f.read().strip().split('\n')

sizes = defaultdict(int)
path = []

for item in disk:
    line = item.strip().split()

    if line[1] == 'cd':
        if line[2] == '..':
            path.pop()
        else:
            path.append(line[2])
    elif line[1] == 'ls':
        continue
    elif line[0] == 'dir':
        continue
    else:
        for i in range(1, len(path) + 1):
            sizes['/'.join(path[:i])] += int(line[0])

result1 = 0
result2 = float('inf')  # max int

for k, v in sizes.items():
    if v <= 100000:
        result1 += v
    if v >= (sizes['/'] - (70000000 - 30000000)):
        result2 = min(result2, v)

print(result1)
print(result2)
