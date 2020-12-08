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

def pc():
    global data
    accumulator = 0
    visited = []
    index = 0
    while(index >= 0):
        com = data[index][0]
        ins = data[index][1]
        if index == len(data)-1:
            return accumulator
        if index in visited:
            return -1
        else:
            if com == 'jmp':
                visited.append(index)
                index += ins
            elif com == 'acc':
                accumulator += ins
                visited.append(index)
                index += 1
            elif com == 'nop':
                visited.append(index)
                index += 1

def change():
    global data
    for k in data:
        if k[0] == 'jmp':
            k[0] = 'nop'
            if pc() > 0:
                return pc()
            else:
                k[0] = 'jmp'
        elif k[0] == 'nop':
            k[0] = 'jmp'
            if pc() > 0:
                return pc()
            else:
                k[0] = 'nop'

print(change())
f.close()
