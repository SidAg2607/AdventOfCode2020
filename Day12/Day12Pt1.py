#I know this is not the shortest or the best solution

f = open('day12text.txt', 'r+')

r = [[x[0], int(x[1:-1])] if x[-1] == '\n' else [x[0], int(x[1:])] for x in f.readlines()]

current = 'E'

pos = [['E', 0], ['S', 0]]

def Path(direction, units):
    global current
    if current == 'E':
        if (direction == 'E') | (direction == 'F'):
            if pos[0][0] == 'E':
                pos[0][1] += units
            else:
                pos[0][1] -= units
        elif direction == 'W':
            if pos[0][0] == 'W':
                pos[0][1] += units
            else:
                pos[0][1] -= units
        elif direction == 'N':
            if pos[1][0] == 'N':
                pos[1][1] += units
            else:
                pos[1][1] -= units
        elif direction == 'S':
            if pos[1][0] == 'S':
                pos[1][1] += units
            else:
                pos[1][1] -= units
        elif ((direction == 'L') | (direction == 'R')) & (units%360 == 180):
            current = 'W'
        elif ((direction == 'L') & (units%360 == 90)) | ((direction == 'R') & (units%360 == 270)):
            current = 'N'
        else:
            current = 'S'
    elif current == 'W':
        if (direction == 'W') | (direction == 'F'):
            if pos[0][0] == 'W':
                pos[0][1] += units
            else:
                pos[0][1] -= units
        elif direction == 'E':
            if pos[0][0] == 'E':
                pos[0][1] += units
            else:
                pos[0][1] -= units
        elif direction == 'N':
            if pos[1][0] == 'N':
                pos[1][1] += units
            else:
                pos[1][1] -= units
        elif direction == 'S':
            if pos[1][0] == 'S':
                pos[1][1] += units
            else:
                pos[1][1] -= units
        elif ((direction == 'L') | (direction == 'R')) & (units % 360 == 180):
            current = 'E'
        elif ((direction == 'L') & (units % 360 == 90)) | ((direction == 'R') & (units % 360 == 270)):
            current = 'S'
        else:
            current = 'N'
    elif current == 'N':
        if direction == 'E':
            if pos[0][0] == 'E':
                pos[0][1] += units
            else:
                pos[0][1] -= units
        elif direction == 'W':
            if pos[0][0] == 'W':
                pos[0][1] += units
            else:
                pos[0][1] -= units
        elif (direction == 'N') | (direction == 'F'):
            if pos[1][0] == 'N':
                pos[1][1] += units
            else:
                pos[1][1] -= units
        elif direction == 'S':
            if pos[1][0] == 'S':
                pos[1][1] += units
            else:
                pos[1][1] -= units
        elif ((direction == 'L') | (direction == 'R')) & (units % 360 == 180):
            current = 'S'
        elif ((direction == 'L') & (units % 360 == 90)) | ((direction == 'R') & (units % 360 == 270)):
            current = 'W'
        else:
            current = 'E'
    elif current == 'S':
        if direction == 'E':
            if pos[0][0] == 'E':
                pos[0][1] += units
            else:
                pos[0][1] -= units
        elif direction == 'W':
            if pos[0][0] == 'W':
                pos[0][1] += units
            else:
                pos[0][1] -= units
        elif direction == 'N':
            if pos[1][0] == 'N':
                pos[1][1] += units
            else:
                pos[1][1] -= units
        elif (direction == 'S') | (direction == 'F'):
            if pos[1][0] == 'S':
                pos[1][1] += units
            else:
                pos[1][1] -= units
        elif ((direction == 'L') | (direction == 'R')) & (units%360 == 180):
            current = 'N'
        elif ((direction == 'L') & (units%360 == 90)) | ((direction == 'R') & (units%360 == 270)):
            current = 'E'
        else:
            current = 'W'

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

print(pos[0][1]+pos[1][1])

f.close()
