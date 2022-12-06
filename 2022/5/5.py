with open('input.txt') as f:
    crates, moves = f.read().split('\n\n')

crates_list = crates.split('\n')
normalize_list = [list(line[1::4]) for line in crates_list[:-1]]

stacks = []
for i in range(len(normalize_list[0])):
    stack = []
    for j in range(len(normalize_list)):
        try:
            if normalize_list[-1 - j][i] != ' ':
                stack.append(normalize_list[-1 - j][i])
        except:
            pass
    stacks.append(stack)

moves_list = [[int(line.split(' ')[1]), int(line.split(' ')[3]) - 1, int(line.split(' ')[5]) - 1]
              for line in moves.strip().split('\n')]

stacks1 = [stack.copy() for stack in stacks.copy()]
for instruction in moves_list:
    to_move = []
    for _ in range(instruction[0]):
        to_move.append(stacks1[instruction[1]].pop())
    stacks1[instruction[2]].extend(to_move)
print(''.join([stack[-1] for stack in stacks1]))

stacks2 = [stack.copy() for stack in stacks.copy()]
for instruction in moves_list:
    to_move = []
    for _ in range(instruction[0]):
        to_move.append(stacks2[instruction[1]].pop())
    to_move.reverse()
    stacks2[instruction[2]].extend(to_move)

print(''.join([stack[-1] for stack in stacks2]))
