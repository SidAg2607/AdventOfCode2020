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


def D2B(decimal):
    binary = ''
    dec = decimal
    while dec >= 1:
        binstr = str(dec % 2)
        binstr += binary
        binary = binstr
        dec = int(dec / 2)
    while len(binary) < 36:
        binary = '0' + binary
    return binary


MemoryRegister = {}


def maskNum(list1):
    global MemoryRegister
    mask = list1[0]
    list2 = list1[1:]
    for num in list2:
        b = D2B(num[1])
        b_masked = ''
        for ind, char in enumerate(b):
            if mask[ind] != 'X':
                b_masked += mask[ind]
            else:
                b_masked += char
        d = B2D(b_masked)
        MemoryRegister.update({num[0]: d})


for item in mask_memory:
    maskNum(item)

sumMemoryValues = 0

for value in MemoryRegister.values():
    sumMemoryValues += value

print(sumMemoryValues)
