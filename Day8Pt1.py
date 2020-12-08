f = open("day8text.txt", "r+")

r = f.readlines()

data = []

for i in r:
    if i[-1] == '\n':
        data.append((i[:-1]).split())
    else:
        data.append(i.split())

for j in data:
    if j[1][0] == '+':
        j[1] = int(j[1][1:])
    else:
        j[1] = int(j[1])

accumulator = 0
visited = []

def pc(index):
    global accumulator, visited
    com = data[index][0]
    ins = data[index][1]
    if index in visited:
        print(accumulator)
    else:
        if com == 'acc':
            accumulator += ins
            visited.append(index)
            pc(index+1)
        elif com == 'jmp':
            visited.append(index)
            pc(index+ins)
        elif com == 'nop':
            visited.append(index)
            pc(index + 1)

pc(0)

f.close()