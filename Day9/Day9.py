f = open("day9text.txt", "r+")

r = [int(x[:-1]) for x in f.readlines()]

r2 = r.copy()


def popfunc():
    global r
    length = len(r)
    for i, l in enumerate(r[:25]):
        for j, k in enumerate(r[:25]):
            if (i != j) and (l + k == r[25]):
                r.pop(0)
                return popfunc()
    if length == len(r):
        return r[25]


z = popfunc()
zindex = r2.index(z)


def contiguous():
    for q, w in enumerate(r2[:zindex]):
        for o, p in enumerate(r2[q + 1:zindex]):
            g = sum(r2[q:r2.index(p) + 1])
            if g == z:
                return max((r2[q:r2.index(p) + 1])) + min((r2[q:r2.index(p) + 1]))
            else:
                pass


print('Part 1:', z)
print('Part 2:', contiguous())

f.close()
