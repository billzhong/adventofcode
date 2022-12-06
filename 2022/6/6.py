with open('input.txt') as f:
    msg = f.read()


def d6(window_size):
    for i in range(len(msg)):
        window = [char for char in msg[i:i + window_size]]
        if len(set(window)) == len(window):
            return i + window_size


print(d6(4))
print(d6(14))
