f = open('day13text.txt', 'r+')

r = f.readlines()

timestamp = int(r[0][:-1])

busIds = [int(x) for x in r[1].split(',') if x!='x']

busIdsMins = []

for i in busIds:
    k = i
    while(k <= timestamp):
        k+=i
    busIdsMins.append(k)

min,ind = busIdsMins[0],0

for j,l in enumerate(busIdsMins):
    if min > l:
        min,ind = l,j

print((min-timestamp)*busIds[ind])



