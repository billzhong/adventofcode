with open('input.txt') as f:
    contents = f.read().strip().split('\n')

total = 0
for rucksack in contents:
    comp1 = rucksack[:len(rucksack) // 2]
    comp2 = rucksack[len(rucksack) // 2:]
    shared = set(comp1).intersection(comp2).pop()
    if shared.islower():
        total += (ord(shared) - 96)
    else:
        total += (ord(shared) - 38)
print(total)

total = 0
for rucksack in range(0, len(contents), 3):
    shared = set(contents[rucksack]).intersection(contents[rucksack + 1], contents[rucksack + 2]).pop()
    if shared.islower():
        total += (ord(shared) - 96)
    else:
        total += (ord(shared) - 38)
print(total)
