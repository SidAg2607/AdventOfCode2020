f = open('day12text.txt', 'r+')

r = [[x[0], int(x[1:-1])] if x[-1] == '\n' else [x[0], int(x[1:])] for x in f.readlines()]

current = [['E', 10], ['N', 1]]

pos = [['E', 0], ['N', 0]]


def Path(direction, units):
    global current, pos
    if direction == 'F':
        if current[0][0] == pos[0][0]:
            pos[0][1] += units * current[0][1]
        else:
            pos[0][1] -= units * current[0][1]
        if current[1][0] == pos[1][0]:
            pos[1][1] += units * current[1][1]
        else:
            pos[1][1] -= units * current[1][1]
    elif direction == 'E':
        if current[0][0] == 'E':
            current[0][1] += units
        else:
            current[0][1] -= units
    elif direction == 'W':
        if current[0][0] == 'W':
            current[0][1] += units
        else:
            current[0][1] -= units
    elif direction == 'N':
        if current[1][0] == 'N':
            current[1][1] += units
        else:
            current[1][1] -= units
    elif direction == 'S':
        if current[1][0] == 'S':
            current[1][1] += units
        else:
            current[1][1] -= units
    elif ((direction == 'L') | (direction == 'R')) & (units % 360 == 180):
        if current[0][0] == 'E':
            current[0][0] = 'W'
        else:
            current[0][0] = 'E'
        if current[1][0] == 'N':
            current[1][0] = 'S'
        else:
            current[1][0] = 'N'
    elif ((direction == 'L') & (units % 360 == 90)) | ((direction == 'R') & (units % 360 == 270)):
        a = current[0][1]
        b = current[1][1]
        if (current[0][0] == 'E') & (current[1][0] == 'N'):
            current[0][1] = b
            current[1][1] = a
            current[0][0] = 'W'
        elif (current[0][0] == 'E') & (current[1][0] == 'S'):
            current[0][1] = b
            current[1][1] = a
            current[1][0] = 'N'
        elif (current[0][0] == 'W') & (current[1][0] == 'N'):
            current[0][1] = b
            current[1][1] = a
            current[1][0] = 'S'
        elif (current[0][0] == 'W') & (current[1][0] == 'S'):
            current[0][1] = b
            current[1][1] = a
            current[0][0] = 'E'
    else:
        a = current[0][1]
        b = current[1][1]
        if (current[0][0] == 'E') & (current[1][0] == 'N'):
            current[0][1] = b
            current[1][1] = a
            current[1][0] = 'S'
        elif (current[0][0] == 'E') & (current[1][0] == 'S'):
            current[0][1] = b
            current[1][1] = a
            current[0][0] = 'W'
        elif (current[0][0] == 'W') & (current[1][0] == 'N'):
            current[0][1] = b
            current[1][1] = a
            current[0][0] = 'E'
        elif (current[0][0] == 'W') & (current[1][0] == 'S'):
            current[0][1] = b
            current[1][1] = a
            current[1][0] = 'N'


for i in r:
    Path(i[0], i[1])
    if pos[0][1] < 0:
        if pos[0][0] == 'E':
            pos[0][0] = 'W'
            pos[0][1] = -pos[0][1]
        else:
            pos[0][0] = 'E'
            pos[0][1] = -pos[0][1]
    if pos[1][1] < 0:
        if pos[1][0] == 'S':
            pos[1][0] = 'N'
            pos[1][1] = -pos[1][1]
        else:
            pos[1][0] = 'S'
            pos[1][1] = -pos[1][1]
    if current[0][1] < 0:
        if current[0][0] == 'E':
            current[0][0] = 'W'
            current[0][1] = -current[0][1]
        else:
            current[0][0] = 'E'
            current[0][1] = -current[0][1]
    if current[1][1] < 0:
        if current[1][0] == 'S':
            current[1][0] = 'N'
            current[1][1] = -current[1][1]
        else:
            current[1][0] = 'S'
            current[1][1] = -current[1][1]
print(pos[0][1] + pos[1][1])

f.close()
