file = open('day7text.txt', 'r+')
r = file.readlines()

# rule line in r = mirrored bronze bags contain 4 muted tomato bags, 4 bright white bags, 1 faded crimson bag.

rules = {}

for i in r:
    rules.update({i[:i.find("bags") - 1]: (i[i.find("contain") + 8:-2]).split(", ")})

# rule line in rules = mirrored bronze: ['4 muted tomato bags', '4 bright white bags', '1 faded crimson bag']

for p, q in rules.items():
    l = []
    for j in q:
        l.append(j[2:])
    rules.update({p: l})

# rule line in rules now = mirrored bronze: ['muted tomato bags', 'bright white bags', 'faded crimson bag']

for f, s in rules.items():
    g = []
    for o in s:
        if o.find('bags') != -1:
            g.append(o.replace(" bags", ""))
        else:
            g.append(o.replace(" bag", ""))
    rules.update({f: g})

# rule line in rules now = mirrored bronze: ['muted tomato', 'bright white', 'faded crimson']

bags = []

for a, b in rules.items():
    if 'shiny gold' in b:
        bags.append(a)


def bagholder():
    global bags
    r = len(bags)
    for a, b in rules.items():
        for i in bags:
            if (i in b) and (a not in bags):
                bags.append(a)
    if r == len(bags):
        return len(bags)
    else:
        return bagholder()


print(bagholder())

file.close()
