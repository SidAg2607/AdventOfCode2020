file = open('day7text.txt', 'r+')
r = file.readlines()

rules = {}

for i in r:
    rules.update({i[:i.find("bags") - 1]: (i[i.find("contain") + 8:-2]).split(", ")})

for f, s in rules.items():
    g = []
    for o in s:
        if o.find('bags') != -1:
            g.append(o.replace(" bags", ""))
        else:
            g.append(o.replace(" bag", ""))
    rules.update({f: g})

# rule line in rules = mirrored bronze: ['4 muted tomato', '4 bright white', '1 faded crimson']

Num = 0


def bagCounter(bag, opp):
    global Num
    for a, b in rules.items():
        if bag == a:
            for j in b:
                Num += opp * int(j[0])
                try:
                    bagCounter(j[2:], int(j[0]) * opp)
                except ValueError:
                    continue


bagCounter('shiny gold', 1)

print(Num)

file.close()
