with open('input.txt') as f:
    map_ = f.read().strip().split('\n')

result = 0
for y in range(len(map_)):
    for x in range(len(map_[0])):
        if y == 0 or y == (len(map_) - 1) or x == 0 or x == (len(map_[0]) - 1):
            result += 1
        else:
            if max(map_[y][:x]) < map_[y][x] or max(map_[y][x + 1:]) < map_[y][x]:
                result += 1
            else:
                y_row = [tree[x] for tree in map_]
                if max(y_row[:y]) < y_row[y] or max(y_row[y + 1:]) < y_row[y]:
                    result += 1

print(result)

result2 = []
for y in range(len(map_)):
    for x in range(len(map_[0])):
        l = 0
        r = 0
        u = 0
        d = 0

        max_l = 0
        max_r = 0
        max_u = 0
        max_d = 0

        for i in reversed(range(x)):
            l += 1
            if map_[y][i] >= map_[y][x]:
                break

        for i in range(x + 1, len(map_[0])):
            r += 1
            if map_[y][i] >= map_[y][x]:
                break

        for i in reversed(range(y)):
            u += 1
            if map_[i][x] >= map_[y][x]:
                break

        for i in range(y + 1, len(map_[0])):
            d += 1
            if map_[i][x] >= map_[y][x]:
                break

        result2.append(l * r * u * d)

print(max(result2))
