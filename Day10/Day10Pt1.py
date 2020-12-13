f = open("day10text.txt", "r+")

r_sorted = sorted([int(x[:-1]) if x[-1] == "\n" else int(x) for x in f.readlines()])

diff1 = 1
diff3 = 1

for i, j in enumerate(r_sorted):
    if i > 0:
        if (j - r_sorted[i - 1]) == 1:
            diff1 += 1
        elif (j - r_sorted[i - 1]) == 3:
            diff3 += 1

print(diff1 * diff3)
f.close()
