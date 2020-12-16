f = open('day13text.txt', 'r+')

r = f.readlines()[1].split(',')

busses = [int(x) if x!='x' else x for x in r]

BusNotX = []
BusNotXIndex = []

for i, j in enumerate(busses):
    if j != 'x':
        BusNotXIndex.append(i)
        BusNotX.append(j)

mods = []

for index, bus in enumerate(BusNotX):
    ot = 0
    while (bus * ot - BusNotXIndex[index] < 0):
        ot += 1
    mods.append(bus * ot - BusNotXIndex[index])

time = 0

res = 1
for x in BusNotX:
    res = res * x

# Remainder theorem
for busindex, bus in enumerate(BusNotX):
    bi = mods[busindex]
    Ni = int(res / bus)
    counter = 1
    while (Ni * counter) % bus != 1:
        counter += 1
    time += Ni * bi * counter

while time>res:
    time -= res

print(res)
print(time)
