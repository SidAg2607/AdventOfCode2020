f = open("day14text.txt", "r+")

r = [x[:-1] if x[-1] == '\n' else x for x in f]

counter = -1

mask_memory = []

for line in r:
    if line[:4] == 'mask':
        counter += 1
        mask_memory.append([line[7:]])
    else:
        mask_memory[counter].append([int(line[line.find("[") + 1:line.find("]")]), int(line[line.find("=") + 1:])])


def B2D(binary):
    decimal = 0
    binary = int(binary)
    binary = str(binary)
    for j, i in enumerate(binary):
        decimal += int(i) * (2 ** (len(binary) - j - 1))
    return decimal


def D2B(decimal, integer):
    binary = ''
    dec = decimal
    while dec >= 1:
        binstr = str(dec % 2)
        binstr += binary
        binary = binstr
        dec = int(dec / 2)
    while len(binary) < integer:
        binary = '0' + binary
    return binary


MemoryRegister = {}


def CreateBinaryComb(stringS, storeValue):
    global MemoryRegister
    comb = stringS.count('X')
    for i in range(2 ** comb):
        stringSx = ''
        strbincomb = D2B(i, comb)
        inccounter = 0
        for w in stringS:
            if w == 'X':
                stringSx += strbincomb[inccounter]
                inccounter += 1
            else:
                stringSx += w
        MemoryRegister.update({B2D(stringSx): storeValue})


def maskNum(list1):
    global MemoryRegister
    mask = list1[0]
    list2 = list1[1:]
    for num in list2:
        memoryLoc = D2B(num[0], 36)
        MaskedS = ''
        for a1, a2 in enumerate(mask):
            if (a2 == '1') | (a2 == 'X'):
                MaskedS += a2
            else:
                MaskedS += memoryLoc[a1]
        CreateBinaryComb(MaskedS, num[1])


for item in mask_memory:
    maskNum(item)

sumMemoryValues = 0

for value in MemoryRegister.values():
    sumMemoryValues += value

print(sumMemoryValues)
