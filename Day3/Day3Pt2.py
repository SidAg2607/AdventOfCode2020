data = open("day3text.txt", "r+")
lines = data.readlines()
NumOfLines = len(lines)
BlockLength = len(lines[0]) - 1

def path(R, D):
    if R % D != 0:
        RightCh = ((NumOfLines - 1) * (int(R / D) + 1)) + 1
    else:
        RightCh = ((NumOfLines - 1) * (int(R / D))) + 1
    RightBlocks = int(RightCh / BlockLength) + 1
    lines2 = []

    for i in range(len(lines)):
        if i != len(lines) - 1:
            j = ((lines[i])[:-1])
            lines2.append(j * RightBlocks)
        else:
            lines2.append(lines[i] * RightBlocks)

    def TreeCounter(p, q, counter, incp, incq):
        p += incp
        q += incq
        if lines2[q][p] == '#':
            counter += 1
        if (NumOfLines - 1) == q:
            return counter
        else:
            return TreeCounter(p, q, counter, R, D)

    return TreeCounter(0, 0, 0, R, D)

print(path(3, 1) * path(1, 1) * path(5, 1) * path(7, 1) * path(1, 2))
