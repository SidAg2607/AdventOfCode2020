data = open("day3text.txt", "r+")
lines = data.readlines()
NumOfLines = len(lines)
BlockLength = len(lines[0]) - 1
RightCh = ((NumOfLines - 1) * 3) + 1
RightBlocks = int(RightCh / BlockLength) + 1
lines2 = []

for i in range(len(lines)):
    if i != len(lines) - 1:
        j = ((lines[i])[:-1])
        lines2.append(j * RightBlocks)
    else:
        lines2.append(lines[i] * RightBlocks)

def R3D1(p, q, counter):
    p += 3
    q += 1
    if lines2[q][p] == '#':
        counter += 1
    if (NumOfLines - 1) == q:
        return counter
    else:
        return R3D1(p, q, counter)

print(R3D1(0,0,0))